
# jos proveriti najoptimalniju opciju, da li YF ima daily average zbog dnevne volatilnosti, podaci se proveravaju 2x dnevno zbog razlike u vremenskim zonama razlicitih berzi, 
# podaci ce se snimati u DB kao JSON string
# potreban je checker da li su podaci generisani i snimljeni, odnosno da li svaki ticker iz liste za prethodni datum ima vrednost u JSON objektu
# await je potreban za ticker generator
# sugestija #1: cene ce biti smestene u JSON file za odredjeni dan, ako je dan, koji je kljuc +1 uzimi staru cenu i novu i izracunaj promenu


# dovoljno je da se podaci uzimaju 1 dnevno i da se racuna promena u odnosu na staru cenu, svaka znacajna promena ce biti izjednacena u vremenskoj seriji


# 1. save stock values into JSON: current_day_prices.json
# 2. contruct data for DB (difference in values=last tday--current day)
# 3. save JSON str in DB 
# 4. overwrite last_day_prices.json with current_day_prices.json
# 5. clear current_day_prices.json