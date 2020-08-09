Backend Developer internship recruitment task.

List of possible arguments:

	'-h', '--help'- Prints all possible arguments and their descriptions.
			Example run: *python main.py --help* 

	'-gp', '--gender_percent'- Print percentage of each gender in database. 
				   No arguments necessary. 
				   Example run: *python main.py -gp*

	'-aa', '--average_age'- Print global average age and average for each gender. 
				No arguments necessary. 
				Example run: *python main.py -aa*

	'-bp', '--best_passwd' - Prints best password base on a few contition like length.
        			 No arguments necessary. 
				 Example run: *python main.py --best_passwd*

	'-pc', '--most_popular_cities' - Prints list of most popular cities in database.
            				 Require one integer argument to determent list length.
					 Example run: *python main.py --most_popular_cities 10*

	'-pp', '--most-common-passwords' - Prints list of most popular passwords in database. 
					   Require one integer argument to determent list length.
					   Example run: *python main.py --most_common_passwords 5*

        '-bb', '--born_between' - Prints list of people born between two dates.
            			  Require two arguments in format "YYYY-MM-DD".
				  Example run: *python main.py -bb '1966-01-01' '1967-01-01'*
