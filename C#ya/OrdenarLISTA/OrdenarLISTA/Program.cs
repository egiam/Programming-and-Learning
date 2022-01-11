using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OrdenarLISTA
{
    class Ordenar
    {
        private int[] vector;
        private string linea;
        private int n;

        public void init()
        {
            Console.Write("Coloque la cantidad de elementos del vector: ");
            linea = Console.ReadLine();
            n = int.Parse(linea);
            vector = new int[n];

            for (int f=0; f < vector.Length; f++)
            {
                Console.Write("Coloque el elemento N" + (f+1)+": ");
                linea = Console.ReadLine();
                vector[f] = int.Parse(linea);

            }

            
        }

        public void ordenar()
        {
            for (int k = 0; k < vector.Length; k++)
            {
                for (int f = 0; f < vector.Length - 1 - k; f++)
                {
                    if (vector[f].CompareTo(vector[f + 1]) > 0)
                    {
                        int aux;
                        aux = vector[f];
                        vector[f] = vector[f + 1];
                        vector[f + 1] = aux;

                    }

                }

            }

           
        }

        public void imprimir()
        {
            Console.WriteLine("Vector ordenados de menor a mayor.");
            for (int f = 0; f < vector.Length; f++)
            {
                Console.WriteLine(vector[f]);

            }

        }


    }


    class Program
    {
        static void Main(string[] args)
        {
            Ordenar o1 = new Ordenar();
            o1.init();
            o1.ordenar();
            o1.imprimir();
            Console.ReadKey();

        }
    }
}
