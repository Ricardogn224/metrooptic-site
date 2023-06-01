# Description: Afficher les enregistrements DNS d'une adresse

import dns.resolver
# Définir l'adresse que nous voulons chercher
adresse = "hepiratebay.org"

# Obtenir les enregistrements DNS associés à l'adresse
enregistrements_dns = dns.resolver.resolve(adresse, 'A')

# Afficher les résultats
print("Enregistrements DNS pour", adresse)
for enregistrement in enregistrements_dns:
    print(enregistrement.to_text())
