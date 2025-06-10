""" Øvelse: "Calculator"

Som altid, læs hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning i kopien.

-------

Opret et program, der fungerer som en simpel lommeregner. Programmet skal fungere som følger:
    1. Forklar brugeren hvordan man betjener programmet.
    2. Præsenter en menu med følgende muligheder:
        - Addition
        - Subtraktion
        - Multiplikation
        - Division
        - Afslut
    3. Bed brugeren om at vælge en mulighed fra menuen.
    4. Hvis brugeren vælger en aritmetisk operation, bed om to tal.
    5. Udfør den valgte operation og vis resultatet.
    6. Gentag processen, indtil brugeren vælger at afslutte.

-------

Hvis du går i stå, spørg Google, andre elever, en AI eller læreren.

Når dit program er færdigt, skub det til dit GitHub-repository.
Send derefter denne Teams-besked til din lærer: `<filnavn> færdig`
Fortsæt derefter med den næste fil."""

from rich.console import Console
import beaupy
import os

con = Console()

OPTIONS = """[[green]1[/green]] + (tryk 1)
[[green]2[/green]] - (tryk 2)
[[green]3[/green]] * (tryk 3)
[[green]4[/green]] / (tryk 4)
[[green]5[/green]][red] Afslut! [/red]
"""

def clear():
    os.system("cls||clear")

def main():
    con.print("[bold cyan]Calculator[/bold cyan]")
    con.print("vælg en funktion fra menuen!")

    while True:
        con.print(OPTIONS)

        try:
            option = int(beaupy.prompt("Vælg metode"))
        except ValueError:
            con.print("[bold red]Ugyldigt input. Skriv et tal fra 1 til 5[/bold red]")
            continue
        if option == 5:
            con.print("[bold red]Farvel![/bold red]")
            break
        elif option in [1, 2, 3, 4]:
            try:
                tal1 = float(beaupy.prompt("Skriv første tal: "))
                tal2 = float(beaupy.prompt("Skriv andet tal: "))
            except ValueError:
                con.print("[red]Ugyldigt input. du skal skrive tal[/red]")
                continue

            if option == 1:
                result = tal1 + tal2
                operator = "+"
            elif option == 2:
                result = tal1 - tal2
                operator = "-"
            elif option == 3:
                result = tal1 * tal2
                operator = "*"
            elif option == 4:
                if tal2 == 0:
                    con.print("[red]Du kan ikke dividere med 0![/red]")
                    continue
                result = tal1 / tal2
                operator = "/"
            con.print(f"[green]Resultat:[/green] {tal1} {operator} {tal2} = [bold green]{result}[/bold green]")
        else:
            con.print("[red]Ugyldigt valg. Prøv igen.[/red]")

if __name__ == "__main__":
    clear()
    main()