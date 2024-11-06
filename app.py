from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Données de l'inventaire
inventaire = [
    ["Produit", "Quantité", "Prix"],
    ["Pommes", 20, 0.5],
    ["Bananes", 30, 0.3],
    ["Oranges", 15, 0.7]
]

def afficher_inventaire():
    return inventaire[1:]  # Retourne les produits sans la ligne d'en-tête

@app.route('/')
def home():
    return render_template("index.html", inventaire=afficher_inventaire())

@app.route('/ajouter', methods=['POST'])
def ajouter_produit():
    nom = request.form['nom']
    quantite = int(request.form['quantite'])
    prix = float(request.form['prix'])
    inventaire.append([nom, quantite, prix])
    return redirect(url_for('home'))

@app.route('/mettre_a_jour', methods=['POST'])
def mettre_a_jour_quantite():
    nom = request.form['nom']
    quantite = int(request.form['quantite'])
    for produit in inventaire[1:]:
        if produit[0] == nom:
            produit[1] = quantite
            break
    return redirect(url_for('home'))

@app.route('/supprimer', methods=['POST'])
def supprimer_produit():
    nom = request.form['nom']
    for produit in inventaire[1:]:
        if produit[0] == nom:
            inventaire.remove(produit)
            break
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
