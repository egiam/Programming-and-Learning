using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FOR
{
    class Program
    {
        static void Main(string[] args)
        {
            int num, suma, i;
            string linea;
            suma = 0;

            for (i = 1; i <= 10; i++)
            {
                Console.Write("Coloque numero: ");
                linea = Console.ReadLine();

                if (i > 5)
                {
                    num = int.Parse(linea);
                    suma = suma + num;
                }
            }

            Console.Write("La suma es: " + suma);
            Console.ReadKey();

            
        }
    }
}
