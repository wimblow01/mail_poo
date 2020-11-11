class Fichier:

    def lire_mails(self, source):
        with open(source, "r") as f:
            contenu = f.read().splitlines()
            f.close

        return contenu