using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WHILE
{
    class Program
    {
        static void Main(string[] args)
        {
            float nota;
            int x, may, men;
            string linea;
            may = 0;
            men = 0;

            x = 1;
            while (x <= 10)
            {
                Console.Write("Coloque la nota del alumno: ");
                linea = Console.ReadLine();
                nota = float.Parse(linea);

                if (nota >= 7)
                {
                    may++;
                }
                else
                {
                    men++;
                }

                x++;
            }

            Console.Write("Cantidad de aprobados: " + may);
            Console.Write("Cantidad de desaprobados: " + men);
            Console.ReadKey();


        }
    }
}
