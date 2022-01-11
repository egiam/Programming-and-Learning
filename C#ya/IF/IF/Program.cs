using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IF
{
    class Program
    {
        static void Main(string[] args)
        {
            int num1, num2, suma, resta, mult, div;
            string linea;

            Console.Write("COloque un numero: ");
            linea = Console.ReadLine();
            num1 = int.Parse(linea);
            Console.Write("COloque otro numero: ");
            linea = Console.ReadLine();
            num2 = int.Parse(linea);

            // If - Condicional

            if (num1 > num2)
            {
                Console.Write("El primer numero es mayor al segundo, la suma de ambos es: ");
                suma = num1 + num2;
                Console.Write(suma);
                Console.Write("El producto de ambos es de: ");
                resta = num1 - num2;
                Console.Write(resta);
            }
            else
            {
                Console.Write("El primer numero no es mayor al segundo, su producto es: ");
                mult = num1 * num2;
                Console.Write(mult);
                Console.Write("Su division es: ");
                div = num1 / num2;
                Console.Write(div);
            }


        }
    }
}
