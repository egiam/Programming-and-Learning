using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LISTAS
{
    class Vectores
    {
        private float[] vector;
        private string linea;
        private float acum, may36, may50;
        private int cant;

        public void init()
        {
            Console.Write("Que cantidad de vectores colocara? ");
            linea = Console.ReadLine();
            cant = int.Parse(linea);
            vector = new float[cant];

            // FOR
            for (int f = 0; f < cant; f++)
            {
                Console.Write("Coloque el " + f + "° elemento del vector");
                linea = Console.ReadLine();
                vector[f] = float.Parse(linea);
                acum = acum + vector[f];

                if (vector[f] > 36)
                {
                    if (vector[f] > 50)
                    {
                        may50++;

                    }

                    may36 = may36 + vector[f];

                }

            }

            // Resultados
            Console.Write("Los vectores son: " + vector);
            Console.Write("El valor acumulado de todos los vectores es: " + acum);
            Console.Write("El valor acumulado de los vectores mayores a 36: " + may36);
            Console.Write("Cantidad de vectores mayores a 50: " + may50);


        }


    }


    class Program
    {
        static void Main(string[] args)
        {
            Vectores vec = new Vectores();
            vec.init();

        }
    }
}
