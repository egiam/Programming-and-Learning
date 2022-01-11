using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CLASES
{
    class Empleado
    {
        private string nombre, linea;
        private int sueldo;


        public void init()
        {
            Console.Write("Ingrese el nombre del empleado: ");
            nombre = Console.ReadLine();
            Console.Write("Ingrese el sueldo: ");
            linea = Console.ReadLine();
            sueldo = int.Parse(linea);

        }

        public void imprimir()
        {
            Console.WriteLine("El empleado: " + nombre + " tiene un sueldo de: " + sueldo);

        }

        public void mensaje()
        {
            if (sueldo > 3000)
            {
                Console.WriteLine("El empleado " + nombre + " debe abonar impuestos");
            }

        }

    }


    class Program
    {
        static void Main(string[] args)
        {
            Empleado emp = new Empleado();
            emp.init();
            emp.imprimir();
            emp.mensaje();
            Console.ReadKey();

        }
    }
}
