import java.util.Scanner;
import java.util.concurrent.TimeUnit;

 class Nim 
{

		int CompAi(int numberLeft)
		{

			int compTakes =0;
			while(true)
				{
					if(numberLeft>8)
					{
						compTakes++;
						if(compTakes == 3||(numberLeft-compTakes) == 8)
						{
							break;
						}
					}
					if(numberLeft<=8 && numberLeft>=4)
					{
						compTakes++;
						if(compTakes == 3 || (numberLeft - compTakes) == 4)
						{
							break;
						}
					}
					if(numberLeft<4)
					{
						compTakes = numberLeft;
						break;
					}
				}

				return compTakes;

		}



		int userInput()
		{

			Scanner sc = new Scanner(System.in);
			int n;
			//System.out.println(": ");
			n = sc.nextInt();
			
			return n;
		}



		public static void main(String args[])
		{
			int numberLeft;
			int userTakes=0;
			int compTakes=0;
			numberLeft = 12;
			Nim ni = new Nim();
			System.out.println("WELCOME TO NIM\n\n");
			System.out.println("The goal of this game is to be the \nfirst person to take away the last coin present\nYou can only take away \n1,2,or 3 coins at once\nCan you beat me, Dr. Nim to it?\n\n");
			System.out.println("\n\nThe number of coins = "+numberLeft);
			while(true)
			{
				System.out.println("\n\nYour Turn....");
				userTakes = ni.userInput();
				if(userTakes<0)
				{
					System.out.println("No, you can't return any coins");
					continue;
				}
				if(userTakes>numberLeft)
				{
					System.out.println("That's more coins than there are on the board!");
					continue;
				}
				if(userTakes>3)
				{
					System.out.println("You can only take away one, two, or 3 coins");
					continue;
				}
				else
				{
					numberLeft = numberLeft - userTakes;
					System.out.println("The number of coins now = "+numberLeft);
					if(numberLeft == 0)
					{
						System.out.println("Congratulations. You have bested me");
						break;
					}
				}

				System.out.println("\n\nIt is now my turn");

				try
				{


					TimeUnit.SECONDS.sleep(2);

				}
				catch(InterruptedException e)
				{
					System.out.println("Caught Exception "+e);
				}


				compTakes = ni.CompAi(numberLeft);
				System.out.println("\n\nI have taken "+compTakes+" coins");
				numberLeft = numberLeft-compTakes;
				System.out.println("The number of coins left now = "+numberLeft);

				try
				{
					TimeUnit.SECONDS.sleep(1);
				}
				catch(InterruptedException e)
				{

					System.out.println("Caught Exception "+e);
				}

				if(numberLeft == 0)
				{
					System.out.println("\nI WIN. You just lost to a bunch of 1s and 0s");
					break;
				}

			}


				

		}
}



	
