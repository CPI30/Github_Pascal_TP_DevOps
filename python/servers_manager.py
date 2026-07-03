import json

# ----- 1. Charger le fichier servers.json -----
with open("servers.json", "r") as fichier:
    serveurs = json.load(fichier)

print("===== 1. Liste des serveurs =====")
for serveur in serveurs:
    print(serveur["name"], "->", serveur["status"])

# ----- 2. Serveurs avec CPU > 80% (a surveiller) -----
print("")
print("===== 2. Serveurs a surveiller (CPU > 80%) =====")
for serveur in serveurs:
    if serveur["cpu_usage"] > 80:
        print(serveur["name"], "-> CPU :", serveur["cpu_usage"], "%")

# ----- 3. Serveurs en panne (status = down) -----
print("")
print("===== 3. Serveurs down =====")
for serveur in serveurs:
    if serveur["status"] == "down":
        print(serveur["name"], "->", serveur["ip"])

# ----- 4. Moyennes CPU et RAM -----
print("")
print("===== 4. Moyennes d'utilisation =====")
total_cpu = 0
total_ram = 0
for serveur in serveurs:
    total_cpu = total_cpu + serveur["cpu_usage"]
    total_ram = total_ram + serveur["ram_usage"]

moyenne_cpu = total_cpu / len(serveurs)
moyenne_ram = total_ram / len(serveurs)
print("Moyenne CPU :", round(moyenne_cpu, 1), "%")
print("Moyenne RAM :", round(moyenne_ram, 1), "%")

# ----- 5. Ajouter un nouveau serveur et sauvegarder -----
print("")
print("===== 5. Ajout d'un nouveau serveur =====")
nouveau_serveur = {
    "name": "srv-new-01",
    "ip": "192.168.5.10",
    "os": "Ubuntu 24.04",
    "region": "eu-west-1",
    "status": "up",
    "cpu_usage": 10,
    "ram_usage": 25
}
serveurs.append(nouveau_serveur)

with open("servers.json", "w") as fichier:
    json.dump(serveurs, fichier, indent=2)

print("Serveur", nouveau_serveur["name"], "ajoute. Total :", len(serveurs), "serveurs.")

# ----- 6. Rapport des serveurs critiques -----
print("")
print("===== 6. Generation du rapport =====")
with open("report.txt", "w") as rapport:
    rapport.write("RAPPORT DES SERVEURS CRITIQUES\n")
    rapport.write("==============================\n")
    for serveur in serveurs:
        raisons = []
        if serveur["status"] == "down":
            raisons.append("serveur down")
        if serveur["cpu_usage"] > 80:
            raisons.append("CPU > 80%")
        if serveur["ram_usage"] > 80:
            raisons.append("RAM > 80%")
        if len(raisons) > 0:
            ligne = serveur["name"] + " : " + ", ".join(raisons) + "\n"
            rapport.write(ligne)

print("Rapport genere : report.txt")
