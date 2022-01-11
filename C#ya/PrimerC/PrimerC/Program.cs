using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PrimerC
{
	class Program
	{
		static void Main(string[] args)
		{
			string helloWorldMessage = "Hello World!!!";

			Console.WriteLine(HelloWorld(helloWorldMessage));
		}

		private static string HelloWorld(string message)
		{
			return message;
		}
	}
}
