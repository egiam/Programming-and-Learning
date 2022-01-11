using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DOWHILE
{
    class Program
    {
        static void Main(string[] args)
        {
            int num, suma;
            string linea;
            suma = 0;

            do
            {
                Console.Write("Coloque numero: ");
                linea = Console.ReadLine();
                num = int.Parse(linea);

                if (num != 9999)
                {
                    suma = suma + num;
                }

            } while (num!=9999);


            Console.Write("El valor acumulado es de: " + suma);
            if (suma > 0)
            {
                Console.Write("El valor es mayor a 0");
            }
            else
            {
                if (suma < 0)
                {
                    Console.Write("El valor es menor a 0");
                }
                else
                {
                    Console.Write("El valor es igual a 0");
                }
            }

        }
    }
}
