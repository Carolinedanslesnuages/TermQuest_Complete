import os
from rich.console import Console

# Initialiser la console pour afficher le texte
console = Console()

# Chapitre 1 : Le Recrutement - Décryptage du message
def chapter_one():
    console.print("[bold cyan]Chapitre 1 : Le Recrutement[/]")
    console.print("""
Votre mission commence maintenant. Vous avez reçu un message crypté dans le fichier 'encrypted_message.txt'.
Pour le décrypter, utilisez la commande suivante :

1. Décryptage du message :
    openssl enc -d -aes-256-cbc -in encrypted_message.txt -base64 -out decrypted_message.txt -pass pass:[VOTRE_PASS_PHRASE]
    
Après avoir décrypté le message, cherchez un **code unique** à l’intérieur. Vous devrez entrer ce code pour continuer.
""")
    
    decrypted_message = console.input("Entrez le code trouvé dans le message décrypté : ").strip()
    
    correct_code = "ABC123XYZ"
    
    if decrypted_message == correct_code:
        console.print("[bold green]Code validé ! Mission 1 réussie. Vous pouvez passer à la mission suivante.[/]")
        return True
    else:
        console.print("[bold red]Code incorrect. Veuillez réessayer après avoir décrypté à nouveau le message.[/]")
        return False

# Chapitre 2 : La Première Mission - Analyser les Logs
def chapter_two():
    console.print("[bold cyan]Chapitre 2 : La Première Mission[/]")
    console.print("""
Votre mission est de trouver toutes les lignes contenant 'ERROR' dans le fichier 'access.log' et de les enregistrer dans un nouveau fichier 'critical_errors.txt'.
""")
    
    user_ready = console.input("Avez-vous terminé la mission ? (oui/non) : ").strip().lower()

    if user_ready == "oui":
        if os.path.exists("critical_errors.txt") and "ERROR" in open("critical_errors.txt").read():
            console.print("[bold green]Mission accomplie avec succès ![/]")
            return True
        else:
            console.print("[bold red]Mission échouée. Vérifiez vos actions et réessayez.[/]")
            return False
    else:
        console.print("[italic yellow]Prenez votre temps pour compléter la mission.[/]")
        return False

# Chapitre 3 : Accéder à NexaCorp - Modifier les Permissions
def chapter_three():
    console.print("[bold cyan]Chapitre 3 : Accéder à NexaCorp[/]")
    console.print("""
Votre mission est de modifier les permissions du fichier 'secrets.txt' dans le répertoire 'secure_zone' pour que seul le propriétaire puisse y accéder.
""")
    
    user_ready = console.input("Avez-vous terminé la mission ? (oui/non) : ").strip().lower()

    if user_ready == "oui":
        permissions = oct(os.stat("secure_zone/secrets.txt").st_mode)[-3:]
        if permissions == "600":
            console.print("[bold green]Mission accomplie avec succès ![/]")
            return True
        else:
            console.print("[bold red]Mission échouée. Vérifiez vos actions et réessayez.[/]")
            return False
    else:
        console.print("[italic yellow]Prenez votre temps pour compléter la mission.[/]")
        return False

# Chapitre 4 : Manipulation Avancée de Données
def chapter_four():
    console.print("[bold cyan]Chapitre 4 : Manipulation Avancée de Données[/]")
    console.print("""
Votre mission est de trier les données du fichier 'large_dataset.csv' par la colonne 'Value' et de sauvegarder le résultat dans un nouveau fichier 'sorted_data.csv'.
""")
    
    user_ready = console.input("Avez-vous terminé la mission ? (oui/non) : ").strip().lower()

    if user_ready == "oui":
        if os.path.exists("sorted_data.csv"):
            with open("sorted_data.csv", "r") as sorted_file:
                lines = sorted_file.readlines()
                data_lines = lines[:-1]
                sorted_correctly = all(
                    int(data_lines[i].split(",")[1]) <= int(data_lines[i+1].split(",")[1]) 
                    for i in range(len(data_lines)-1)
                )
                if sorted_correctly:
                    console.print("[bold green]Mission accomplie avec succès ![/]")
                    return True
                else:
                    console.print("[bold red]Les données ne sont pas triées correctement. Essayez à nouveau.[/]")
                    return False
        else:
            console.print("[bold red]Mission échouée. Le fichier 'sorted_data.csv' n'a pas été trouvé.[/]")
            return False
    else:
        console.print("[italic yellow]Prenez votre temps pour compléter la mission.[/]")
        return False

# Chapitre 5 : Transfert de Fichiers Sécurisés
def chapter_five():
    console.print("[bold cyan]Chapitre 5 : Transfert de Fichiers Sécurisés[/]")
    console.print("""
Votre mission est de télécharger un fichier depuis un serveur distant et de le sauvegarder dans le répertoire 'network/'.
""")
    
    user_ready = console.input("Avez-vous terminé la mission ? (oui/non) : ").strip().lower()

    if user_ready == "oui":
        if os.path.exists("network/remote_file.txt"):
            console.print("[bold green]Mission accomplie avec succès ![/]")
            return True
        else:
            console.print("[bold red]Mission échouée. Le fichier 'remote_file.txt' n'a pas été trouvé dans le répertoire 'network/'.[/]")
            return False
    else:
        console.print("[italic yellow]Prenez votre temps pour compléter la mission.[/]")
        return False

# Chapitre 6 : Surveillance des Modifications de Fichiers
def chapter_six():
    console.print("[bold cyan]Chapitre 6 : Surveillance des Modifications de Fichiers[/]")
    console.print("""
Votre mission est de surveiller les modifications apportées au fichier 'watched_file.txt' dans le répertoire 'watched/'. 
""")
    
    user_ready = console.input("Avez-vous terminé la mission ? (oui/non) : ").strip().lower()

    if user_ready == "oui":
        if os.path.exists("modification_log.txt") and os.stat("modification_log.txt").st_size > 0:
            console.print("[bold green]Mission accomplie avec succès ![/]")
            return True
        else:
            console.print("[bold red]Mission échouée. Aucune modification enregistrée dans 'modification_log.txt'.[/]")
            return False
    else:
        console.print("[italic yellow]Prenez votre temps pour compléter la mission.[/]")
        return False

# Chapitre 7 : Compression et Décompression de Fichiers
def chapter_seven():
    console.print("[bold cyan]Chapitre 7 : Compression et Décompression de Fichiers[/]")
    console.print("""
Votre mission est de compresser un fichier dans un fichier tar.gz et de le décompresser dans un répertoire spécifique.
1. Utilisez la commande 'tar' pour compresser :
   tar -czf data.tar.gz data.csv
2. Décompressez-le dans le répertoire 'extracted' :
   tar -xzf data.tar.gz -C extracted/
""")
    
    user_ready = console.input("Avez-vous terminé la mission ? (oui/non) : ").strip().lower()

    if user_ready == "oui":
        if os.path.exists("extracted/data.csv"):
            console.print("[bold green]Mission accomplie avec succès ![/]")
            return True
        else:
            console.print("[bold red]Mission échouée. Le fichier 'data.csv' n'a pas été trouvé dans le répertoire 'extracted/'.[/]")
            return False
    else:
        console.print("[italic yellow]Prenez votre temps pour compléter la mission.[/]")
        return False

# Chapitre 8 : Créer un Système de Sauvegarde Automatique
def chapter_eight():
    console.print("[bold cyan]Chapitre 8 : Créer un Système de Sauvegarde Automatique[/]")
    console.print("""
Votre mission est de mettre en place un système de sauvegarde automatique avec 'rsync'.
1. Utilisez la commande 'rsync' pour sauvegarder 'important_data' vers 'backup' :
   rsync -av important_data/ backup/
""")
    
    user_ready = console.input("Avez-vous terminé la mission ? (oui/non) : ").strip().lower()

    if user_ready == "oui":
        if os.path.exists("backup/"):
            console.print("[bold green]Mission accomplie avec succès ![/]")
            return True
        else:
            console.print("[bold red]Mission échouée. Le répertoire de sauvegarde 'backup/' n'a pas été trouvé.[/]")
            return False
    else:
        console.print("[italic yellow]Prenez votre temps pour compléter la mission.[/]")
        return False

# Chapitre 9 : Gestion des Processus en Temps Réel
def chapter_nine():
    console.print("[bold cyan]Chapitre 9 : Gestion des Processus en Temps Réel[/]")
    console.print("""
Votre mission est de surveiller les processus et de tuer un processus spécifique.
1. Utilisez 'ps aux' pour surveiller les processus.
2. Utilisez 'kill PID' pour arrêter un processus spécifique.
""")
    
    user_ready = console.input("Avez-vous terminé la mission ? (oui/non) : ").strip().lower()

    if user_ready == "oui":
        console.print("[bold green]Mission accomplie avec succès ![/]")
        return True
    else:
        console.print("[italic yellow]Prenez votre temps pour compléter la mission.[/]")
        return False

# Chapitre 10 : Sécurisation des Communications
def chapter_ten():
    console.print("[bold cyan]Chapitre 10 : Sécurisation des Communications[/]")
    console.print("""
Votre mission est de vous connecter à un serveur distant via SSH et d'exécuter une commande.
1. Utilisez la commande 'ssh' pour vous connecter et afficher le contenu d'un répertoire :
   ssh user@remote_server 'ls /home/user/'
""")
    
    user_ready = console.input("Avez-vous terminé la mission ? (oui/non) : ").strip().lower()

    if user_ready == "oui":
        console.print("[bold green]Mission accomplie avec succès ![/]")
        return True
    else:
        console.print("[italic yellow]Prenez votre temps pour compléter la mission.[/]")
        return False

# Fonction pour démarrer le jeu
def start_game():
    console.print("[bold cyan]=== Bienvenue dans TermQuest : Ultimate ===[/]")
    name = console.input("[bold yellow]Entrez votre nom : [/]").strip()
    
    console.print(f"[bold green]Bienvenue, {name}. Préparez-vous pour votre première mission ![/]")
    
    # Commencer les chapitres
    chapter_completed = False
    chapters = [chapter_one, chapter_two, chapter_three, chapter_four, chapter_five, chapter_six, chapter_seven, chapter_eight, chapter_nine, chapter_ten]
    
    for chapter in chapters:
        chapter_completed = False
        while not chapter_completed:
            chapter_completed = chapter()

    console.print(f"[bold green]Félicitations {name}, vous avez terminé toutes les missions ![/]")

# Démarrer le jeu
if __name__ == "__main__":
    start_game()