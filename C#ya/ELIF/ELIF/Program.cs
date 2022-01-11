using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ELIF
{
    class Program
    {
        static void Main(string[] args)
        {
            int num1, num2, num3;
            string linea;

            Console.Write("Coloque el primer numero: ");
            linea = Console.ReadLine();
            num1 = int.Parse(linea);
            Console.Write("Coloque el segundo numero: ");
            linea = Console.ReadLine();
            num2 = int.Parse(linea);
            Console.Write("Coloque el tercer numero: ");
            linea = Console.ReadLine();
            num3 = int.Parse(linea);

            // IF

            if (num1 > num2 & num1 > num3){
                Console.Write("El mayor es el primer numero: " + num1);
            }
            else
            {
                if (num2 > num3)
                {
                    Console.Write("El mayor es el segundo numero: " + num2);
                }
                else
                {
                    Console.Write("El mayor es el tercer numero: " + num3);
                }
            }
            Console.ReadKey();

            if (num1 < 10 || num2 < 10 || num3 < 10)
            {
                Console.Write("Alguno de los numeros es menor a 10");
            }

        }
    }
}
