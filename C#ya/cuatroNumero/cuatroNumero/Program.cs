using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace cuatroNumero
{
    class Program
    {
        static void Main(string[] args)
        {
            int num1, num2, num3, num4, suma, mult;
            string linea;

            Console.Write("Coloque un numero: ");
            linea = Console.ReadLine();
            num1 = int.Parse(linea);
            Console.Write("Coloque otro numero: ");
            linea = Console.ReadLine();
            num2 = int.Parse(linea);
            Console.Write("Coloque otro numero: ");
            linea = Console.ReadLine();
            num3 = int.Parse(linea);
            Console.Write("Coloque otro numero: ");
            linea = Console.ReadLine();
            num4 = int.Parse(linea);


            Console.Write("La suma de los dos primeros numeros es: ");
            suma = num1 + num2;
            Console.Write(suma);
            Console.Write("El producto de los dos ultimos numeros es: ");
            mult = num3 * num4;
            Console.Write(mult);
            Console.ReadKey();

        }
    }
}
