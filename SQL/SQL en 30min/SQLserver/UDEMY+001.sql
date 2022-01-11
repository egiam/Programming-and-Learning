
--DROP TABLE CLIENTES;
----------------------------------------
--   CREA LAS TABLAS
----------------------------------------
CREATE TABLE CLIENTES
(
	CD_CLIENTE          VARCHAR2(10) NOT NULL ,
	ST_NOMBRE           VARCHAR2(30) NULL ,
	TX_DIRECCION        VARCHAR2(200) NULL ,
	ST_STATUS 			CHAR(1) NULL CONSTRAINT CONSTRAINT001 CHECK (ST_STATUS IN ('S','N')),
	NU_NUMERO1          NUMBER NULL ,
	NU_NUMERO2          NUMBER NULL ,
	FH_FECHA            DATE NULL
);

----------------------------------------
--   CREA LOS INDICES
----------------------------------------
CREATE UNIQUE INDEX CLIENTE_001 ON CLIENTES
(
    CD_CLIENTE ASC,
    ST_NOMBRE  ASC
);

----------------------------------------
--   CREA LA LLAVE PRIMARIA
----------------------------------------
ALTER TABLE CLIENTES
ADD CONSTRAINT CLIENTE_001 PRIMARY KEY 
(
    CD_CLIENTE,
    ST_NOMBRE
);

--------------------------------------------------------
-- CARGA DE DATOS GLOBAL
--------------------------------------------------------
INSERT INTO CLIENTES (CD_CLIENTE ,ST_NOMBRE  ,TX_DIRECCION   ,ST_STATUS  ,NU_NUMERO1 ,NU_NUMERO2 ,FH_FECHA) 
VALUES               ( 1         ,'CLIENTE1' ,'CALLE 12'     ,'S'        ,1000       ,2000       ,'10/10/2025');
COMMIT;

SELECT * FROM CLIENTES; 










----------------------------------------
--   CREA LAS LLAVES FORANEAS O FOREIGN KEY
----------------------------------------
ALTER TABLE CLIENTES
	ADD (CONSTRAINT R0370021 FOREIGN KEY (CD_SECTOR) REFERENCES GORAPR.TSCA037_SECTOR (CD_SECTOR));
	
ALTER TABLE GORAPR.TSCA003_OFICINA
	ADD (CONSTRAINT R0640031 FOREIGN KEY (CD_LOCALIDAD) REFERENCES GORAPR.TSCA064_LOCALIDAD (CD_LOCALIDAD));

----------------------------------------
--   OTORGA PRIVILEGIOS DE ACCESSO
----------------------------------------
GRANT SELECT, INSERT, UPDATE, DELETE ON CLASE1.CLIENTES TO CLASE1;
COMMIT;



--DELETE FROM CLASE1.CLIENTES;
--COMMIT;
--------------------------------------------------------
-- CARGA DE DATOS GLOBAL
--------------------------------------------------------

----------------------------------------
--   CREA LOS PROCEDIMIENTOS
----------------------------------------
CREATE OR REPLACE
procedure p_log(pp_cadena varchar2) is
    begin
            dbms_output.put_line( pp_cadena );
    end p_log;
    ------------------------------------------------------------------------------------------
    procedure p_depura(pp_cadena varchar2) is
    begin
        if v_depura then
            dbms_output.put_line( pp_cadena );
        end if;
    end p_depura;
    ------------------------------------------------------------------------------------------
    procedure p_asigna_folios_consultor is
    /****************************************************************************
    C100 SICA V10.0
    RQ01 – Pantalla Asignación de Casos
    FN02 – Asignación de casos Automática 
    Crear proceso batch que asigne automáticamente los folios de las alertas al 
    consultor definido por cada Tipología (Parametria: Asignación por Tipología).
    *****************************************************************************/
    TYPE rec_consultores IS RECORD(
      a_asignar          varchar2(8),
      tope_asignado      integer,
      tipologia          varchar2(2),
      ya_asigno          varchar2(1)      
    );
    TYPE tip_tab_consultores IS TABLE OF rec_consultores INDEX BY BINARY_INTEGER;
    tab_cnsltrs tip_tab_consultores;
    cursor cur_consultores is
       select cd_usr_consultor quien,nu_tope_alertas tope,cd_tipologia tipologia
       from   GORAPR.TSCA047_ASIG_TPLG
       where  (nu_tope_alertas,cd_usr_consultor)
                   not in (select count(1) cuantos,cd_usuario_asignado asignado
                           from   GORAPR.TSCA014_CASO
                           where  cd_st_caso in (C_CDSTCS_ANLSS,C_CDSTCS_RNLSS)
                           group by cd_usuario_asignado)
       and    cd_usr_consultor in (select cd_usuario
                                   from   GORAPR.TSCA024_USUARIO 
                                   where  cd_st_sistema = C_CD_ST_SSTM_ACTV /*'ACTIVO'*/
                                   );
    ----Constantes para el procedimiento, Valores a asignar -----------------------------------
    C_DICT_PREL       constant varchar2(10)  :='DESCARTAR';
    C_JSTFCCN_1       constant varchar2(100) :='DESCARTE TIENE ALERTAS PREVIAS NO MAYORES A 6 MESES';
    C_JSTFCCN_2       constant varchar2(100) :='DESCARTE CUENTA CANCELADA';
    C_JSTFCCN_3       constant varchar2(100) :='DESCARTE NO CUMPLE CON MATRIZ DE CRITERIOS';
    C_JSTFCCN_4       constant varchar2(100) :='DESCARTE NO CUMPLE CON EL MODELO';
    C_JSTFCCN_5       constant varchar2(100) :='DESCARTE TIENE ALERTAS PREVIAS EN SICA NO MAYORES A 3 MESES';

    ------------------------------------------------------------------------------------------
    cursor cur_alertas is
        select x.nu_folio_alerta,x.nu_cuenta, x.cd_cliente,x.tipologia,x.score_mc,x.score_mdl,
               x.sector,x.umbral
              from (
        select nu_folio_alerta,nu_cuenta,cd_cliente,cd_tipologia tipologia,score_mc,score_mdl,
              (SELECT max(cd_sector) 
               FROM   GORAPR.TSCA016_CLIENTE c
               where  c.cd_cliente = a.cd_cliente) sector,
              (SELECT nu_umbral_mc 
               from   GORAPR.TSCA007_TIPOLOGIA u
               where  u.cd_tipologia = a.cd_tipologia) umbral
        from   GORAPR.TSCA013_ALERTA a 
        where  a.cd_st_alerta not in (C_CDSTALRT_DSCRTD)
        and    a.cd_tipologia in (select cd_tipologia 
                                  from   GORAPR.TSCA047_ASIG_TPLG 
                                  where  CD_TP_ASIGNACION =(select cd_det_catalogo 
                                                            from   GORAPR.TSCA018_DET_CATALOG
                                                            where  CD_CATALOGO = C_CAT_ASGNCN
                                                            and    nb_valor    = C_TP_ASGNCN 
                                                            ))
        and    a.cd_st_alerta = C_CDSTALRT_PNDNT ) x;       ----Solo las automaticas
    -----------------------------------------------
    cursor cur_cancelados(pc_cuenta in varchar2, pc_cliente in varchar2) is
        select 'CANCELADO' dictamen 
        from   GORAPR.TSCA017_CUENTA c 
        where  c.nu_cuenta = pc_cuenta and ST_CUENTA='C';
    -----------------------------------------------cur_previas_6m
    cursor cur_previas_6m(pc_cuenta in varchar2, pc_cliente in varchar2) is 
        SELECT 'DESCARTAR' dictamen, /*T38.NU_CASO,*/ 
               t05.nu_cliente, substr(t05.nu_cuenta,11,10) as nu_cuenta,
               substr(t05.tx_operacion_repor,0,2) as cd_tipologia
               ----,t05.fh_deteccion as fh_alerta
        FROM   
                TSA005_OPER_HIST t05
               ,TSA038_CASO      t38
        WHERE  t05.nu_folio_pld  =       t38.nu_folio_pld
        and    (t05.fh_deteccion between add_months(sysdate,-6) and sysdate)
        and    t05.nu_cliente    =       pc_cliente;            
    ----------------------------------------------------------cur_previas_3m----
    cursor cur_previas_3m(pc_cuenta in varchar2, pc_cliente in varchar2) is 
        select 'DESCARTAR' dictamen,h.nu_cuenta
        from   GORAPR.TSCA013_ALERTA h
        where  (h.FH_ALERTA between add_months(sysdate,-3) and sysdate )
        and    cd_cliente = pc_cliente;
    ----------------------------------------------------------------------------
    v_CD_ST_ALERTA          number      := null;
    v_TX_MOTIVO_DESCARTE    varchar2(200);
    v_num_caso              number;
    v_existe_caso           varchar2(2) :='NO';
    v_num_consultor         integer     :=1;
    v_ultimo_consltr        integer;
    v_cd_consultor_asigna   varchar2(8);
    v_cadenota              varchar2(1000);
    -----------------------------------------------
    procedure p_llena_consultores is
    begin
        ----------------------Llena de consultores que se crearan con el caso----------------
        for a in cur_consultores loop
           tab_cnsltrs(v_num_consultor).a_asignar     := a.quien;
           tab_cnsltrs(v_num_consultor).tope_asignado := a.tope;
           tab_cnsltrs(v_num_consultor).tipologia     := a.tipologia;
           tab_cnsltrs(v_num_consultor).ya_asigno     := 'N';
           v_ultimo_consltr := v_num_consultor;
           v_num_consultor  := v_num_consultor + 1;
        end loop;
    end p_llena_consultores;
    ----------------------------------------------------------------------------------------
    function f_busca_consultor(pf_tipol varchar2) return varchar2 is
        v_retorna varchar2(8);
        v_cuantos number;
    begin
        for i in 1..v_ultimo_consltr loop
            if     tab_cnsltrs(i).ya_asigno = 'N' 
               and tab_cnsltrs(i).tipologia = pf_tipol then
               tab_cnsltrs(i).ya_asigno := 'S';
               v_retorna := tab_cnsltrs(i).a_asignar;
            end if;
        end loop;
        ---------
        if v_retorna is null then -----------para una segunda vuelta en caso de pasar el tope-- 
            for i in 1..v_ultimo_consltr loop
                if     tab_cnsltrs(i).ya_asigno = 'S' 
                   and tab_cnsltrs(i).tipologia = pf_tipol then
                   v_retorna := tab_cnsltrs(i).a_asignar;
                end if;
                tab_cnsltrs(i).ya_asigno := 'N';
            end loop;
        end if;
        ----------------------------------------------
        select count(1) n_cuantos into  v_cuantos from GORAPR.TSCA014_CASO
            where cd_usuario_asignado = v_retorna;
        --------------------------------------------------------------
        if v_cuantos > tab_cnsltrs(v_num_consultor).tope_asignado then
            return null;
        else
            return v_retorna;
        end if;
    end f_busca_consultor;
    ------------------------------------------------------------------------------------------
     begin
        p_LOG( 'Inicia!: '||to_char(sysdate,'DD-MON-YYYY HH24:MI:SS') );
        p_llena_consultores;
        --------------------------------------------------------
        for i in cur_alertas loop
            begin
                if v_depura then 
                    v_cadenota :=trim(i.nu_folio_alerta)||'|'||trim(i.nu_cuenta)||'|'||
                               trim(i.cd_cliente)||'|'||trim(i.tipologia)||'|'||i.score_mc||'|'||
                                i.score_mdl||'|'||trim(i.sector)||'|'||trim(i.umbral)||'|';
                                --i.puntos_matriz;
                    p_depura( 'Entra!: '||v_cadenota );
                end if;
                -------------------------------------------------------1a Regla
                if v_CD_ST_ALERTA is null then
                    p_depura( 'Entra:1' );
                    for p6 in cur_previas_6m(i.nu_cuenta,i.cd_cliente) loop
                        if p6.dictamen = C_DICT_PREL then
                            v_CD_ST_ALERTA := C_CDSTALRT_DSCRTD;
                            v_TX_MOTIVO_DESCARTE := C_JSTFCCN_1;
                        end if;
                    end loop;
                end if;
                -------------------------------------------------------2a Regla
                if v_CD_ST_ALERTA is null then
                    p_depura( 'Entra:2' );
                    for c in cur_cancelados(i.nu_cuenta,i.cd_cliente) loop
                        if c.dictamen = 'CANCELADO' then
                            v_CD_ST_ALERTA := C_CDSTALRT_DSCRTD;
                            v_TX_MOTIVO_DESCARTE := C_JSTFCCN_2;
                        end if;
                    end loop;
                end if;
                -------------------------------------------------------3a Regla
                if v_CD_ST_ALERTA is null then
                    p_depura( 'Entra:3' );
                    if i.score_mc < i.umbral then
                        v_CD_ST_ALERTA := C_CDSTALRT_DSCRTD;
                        v_TX_MOTIVO_DESCARTE := C_JSTFCCN_3;
                    end if;
                end if;
                -------------------------------------------------------4a Regla
                if v_CD_ST_ALERTA is null then
                    p_depura( 'Entra:4' );
                    if  (i.score_mdl = 0) and 
                       (i.score_mc  = i.umbral or i.score_mc > i.umbral) then
                        v_CD_ST_ALERTA := C_CDSTALRT_DSCRTD;
                        v_TX_MOTIVO_DESCARTE := C_JSTFCCN_4;
                    end if;
                end if;
                -------------------------------------------------------5a Regla
                if v_CD_ST_ALERTA is null then
                    p_depura( 'Entra:5' );
                    for p3 in cur_previas_3m(i.nu_cuenta,i.cd_cliente) loop
                        if p3.dictamen = C_DICT_PREL then
                            v_CD_ST_ALERTA := C_CDSTALRT_DSCRTD;
                            v_TX_MOTIVO_DESCARTE := C_JSTFCCN_5;
                        end if;
                    end loop;
                end if;
                ------------------------------------------------------------------------
                p_depura( '???var:<'||v_CD_ST_ALERTA||'> txt:<'||v_TX_MOTIVO_DESCARTE||'>');
                ------------------------------------------------------------------------
                if not v_depura then  ----No se realizan transacciones!!!----
                    if v_CD_ST_ALERTA<>C_CDSTALRT_DSCRTD or 
                       v_CD_ST_ALERTA is null then
                            v_CD_ST_ALERTA := C_CDSTCS_ANLSS; ----Asigno!-------
                            p_depura( 'Asigna...'||v_CD_ST_ALERTA );
                        begin ----En Análisis,En Supervision o Reanalisis ?-----
                            select nvl(max(cd_caso),0),'SI' INTO v_num_caso,v_existe_caso
                            from GORAPR.TSCA014_CASO
                            where cd_caso    in (select cd_caso from GORAPR.TSCA013_ALERTA 
                                                 where  cd_cliente = i.cd_cliente )
                            and   cd_st_caso in (C_CDSTCS_ANLSS); --,C_CDSTCS_SPRVSN,C_CDSTCS_RNLSS); 
                            ----Descartadas, Liberada a SIA o no asignado!----
                        exception when no_data_found then
                              select nvl(SQ_TSCA014.nextval,0) into v_num_caso from dual;
                              v_existe_caso :='NO';
                        end;
                        p_depura( 'v_num_caso buscado:<'||v_num_caso||'>');
                        if v_num_caso = 0 then
                             begin
                                select gorapr.SQ_TSCA014.nextval into v_num_caso from dual;
                                p_depura( 'v_num_caso asignado:<'||v_num_caso||'>');
                                v_cd_consultor_asigna := f_busca_consultor(i.tipologia);
                                p_log( 'Caso a:'||v_cd_consultor_asigna||
                                                     ' caso #:'||v_num_caso||
                                                     ' cliente:'||i.cd_cliente||
                                                     ' fecha:'||sysdate||
                                                     ' status:'||C_CDSTCS_ANLSS );
                                if v_cd_consultor_asigna is not null then ----Si obtiene consultor lo asigna
                                    insert into GORAPR.TSCA014_CASO  ----------------------------Asignar caso
                                        (cd_usuario_asignado, cd_st_caso,   cd_caso, tp_justif,fh_dictamen_pre,cd_cliente)
                                    values
                                        (v_cd_consultor_asigna,C_CDSTCS_ANLSS,v_num_caso,'ASIGNACION',sysdate,   i.cd_cliente);
                                end if;
                             exception 
                                when others then 
                                    p_log('TSCA014_CASO:'|| SQLERRM );
                             end;
                        end if;
                        -------------------------------------
                        if v_cd_consultor_asigna is not null then ----Si obtiene consultor lo asigna
                           begin
                              update GORAPR.TSCA013_ALERTA set 
                                         CD_ST_ALERTA  = v_CD_ST_ALERTA,
                                        cd_caso       = v_num_caso,
                                        fh_asignacion = sysdate
                              where  nu_folio_alerta = i.nu_folio_alerta 
                              and    cd_cliente      = i.cd_cliente
                              and    nu_cuenta       = i.nu_cuenta;
                              commit;
                              p_log( 'Alerta a caso?:['||v_num_caso||']' );
                           exception 
                              when others then 
                                p_log('TSCA013_ALERTA:'|| SQLERRM );
                           end;
                        end if; ----Si no sigue pendiente de asignacion----
                    else ----------------------------------------DESCARTA-----
                          begin
                             p_log( 'Alerta folio:'||i.nu_folio_alerta||
                                                  ' cliente:'||i.cd_cliente||
                                                  ' cuenta:'||i.nu_cuenta||
                                                  ' por:'||v_TX_MOTIVO_DESCARTE);
                             update GORAPR.TSCA013_ALERTA set 
                                        CD_ST_ALERTA       = v_CD_ST_ALERTA,
                                        TX_MOTIVO_DESCARTE = v_TX_MOTIVO_DESCARTE,
                                        FH_ASIGNACION      = sysdate
                             where  nu_folio_alerta = i.nu_folio_alerta 
                             and    cd_cliente      = i.cd_cliente
                             and    nu_cuenta       = i.nu_cuenta;
                             commit;
                          exception 
                             when others then p_log('TSCA013_ALERTA:'|| SQLERRM );
                          end;
                    end if;
                end if; ----Depuracion----
            exception 
               when others then p_log( SQLERRM );
            end;
            ---------------------------
            v_CD_ST_ALERTA       := null;
            v_TX_MOTIVO_DESCARTE := null;            
        end loop;
        p_LOG( 'Termina!: '||to_char(sysdate,'DD-MON-YYYY HH24:MI:SS') );
        -----------------------------------------------------------------
     EXCEPTION when others then
            p_log('p_asigna_folios_consultor:'|| SQLERRM );
     END p_asigna_folios_consultor;