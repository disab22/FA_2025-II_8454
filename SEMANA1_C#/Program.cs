using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace S01_C_
{
    internal class Program

    {
        static void Main(string[] args)

        {
            EJER_5();
            Console.ReadKey();
        }
        static void EJER_1()

        {
            String nombre, carrera;
            Console.WriteLine("Ingrese su nombre: ");
            nombre = Console.ReadLine();
            Console.WriteLine("Ingrese su carrera: ");
            carrera = Console.ReadLine();
            Console.WriteLine($"\n{nombre}, Bienvenido al curso de Fundamentos de Algoritmos de la carrera {carrera}");
     
        }
        static void EJER_2()

        {
           Console.WriteLine("\"Allison\"");
        }

        static void EJER_3()

        {
            Console.Write("Ingrese numero 1:");
            int num1=int.Parse(Console.ReadLine());

            Console.Write("Ingrese numero 2:");
            int num2=int.Parse(Console.ReadLine());

            double divi = (double)num1 / (double)num2;

            Console.WriteLine("\nSuma: " + (num1 + num2));
            Console.WriteLine("Resta: " + (num1 + num2));
            Console.WriteLine("Multiplicacion: " + (num1 * num2));
            Console.WriteLine("Division: " + divi);
        }

        static void EJER_4()

        {
            Console.Write("Ingrese un numero decimal: ");
            double num=double.Parse(Console.ReadLine());    

            double raiz2=Math.Sqrt(num);
            double redo=Math.Round(num,0);
            double cubo=Math.Pow(num,3);
            double raiz3=Math.Pow(num,1/3d);

            Console.WriteLine("\nRaiz 2: " +raiz2);
            Console.WriteLine("Redondeando:"+redo);
            Console.WriteLine("Al cubo:" + cubo);
            Console.WriteLine("Raiz cubica:" + raiz3);
        }

        static void EJER_5()

        {
            Console.Write("Ingrese un numero: ");
            string num=Console.ReadLine();

            int entero=int.Parse(num);  
            double deci=double.Parse(num);

            Console.WriteLine("\nResto: "+(entero % 2));
            Console.WriteLine("Dividido 3: " + (deci / 3));
        }

        static void EJER_6()

        {



        }

    }

}