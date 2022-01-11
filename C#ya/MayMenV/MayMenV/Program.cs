using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MayMenV
{
    class MayMen
    {
        private int[] vector;
        private int may, men, rep;

        public void init()
        {
            int n;
            string linea;

            Console.Write("Coloque la cantidad de elementos a colocar: ");
            linea = Console.ReadLine();
            n = int.Parse(linea);

            for (int f=0; f >= n; f++)
            {
                Console.Write("Coloque el elemento: ");
                linea = Console.ReadLine();
                vector[f] = int.Parse(linea);

            }

        }

        public void May()
        {
            may = vector[0];
            men = vector[0];

            for (int f = 1; f == vector.Length; f++)
            {
                if (vector[f] >= may)
                {
                    may = vector[f];

                    if (vector[f] == may)
                    {
                        rep = 1;

                    }
                    else
                    {
                        rep = 0;

                    }
                                        
                }
                else
                {
                    if (vector[f] <= men)
                    {
                        men = vector[f];

                        if (vector[f] == men)
                        {
                            rep = 1;

                        }
                        else
                        {
                            rep = 0;

                        }

                    }
                    
                }
                             
            }

            // separador

            Console.Write("El menor de los elementos: " + men);
            if (rep == 1)
            {
                Console.Write("Ese numero se repite");

            }


        }

    }


    class Program
    {
        static void Main(string[] args)
        {
            MayMen m1 = new MayMen();
            m1.init();
            m1.May();

        }
    }
}
