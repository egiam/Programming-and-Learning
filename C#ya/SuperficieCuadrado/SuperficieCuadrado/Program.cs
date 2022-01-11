using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SuperficieCuadrado
{
    class Program
    {
        static void Main(string[] args)
        {
            float lado;
            float sup;
            string linea;

            Console.Write("Ingrese el valor del lado del cuadrado: ");
            linea = Console.ReadLine();
            lado = float.Parse(linea);
            Console.Write("La superficie del cuadrado es: ");
            sup = lado * lado;
            Console.Write(sup);
            Console.ReadKey();
        }
    }
}
