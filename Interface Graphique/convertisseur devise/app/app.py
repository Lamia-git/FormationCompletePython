from PySide2 import QtWidgets
import currency_converter
class App(QtWidgets.QWidget): #la fenetre graphique 
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Convertisseur de devise")
        #instancier la classe CurrencyConverter Pour importer les devise
        self.devise = currency_converter.CurrencyConverter()
        self.setup_ui()
        self.SetdefaultValues()
        self.setup_connection()
        self.setup_css()
    
    
    #creer le contenu de ma fenetre   
    def setup_ui(self):
        #creation de layout pour positionner notre different widget
        self.layout = QtWidgets.QHBoxLayout(self) #self pour parenter le leyaout a notre fenêtre 
        #combobox
        self.ccb_device_from = QtWidgets.QComboBox()
        #spinbox
        self.spn_montant = QtWidgets.QSpinBox()
        #combox pour devise to
        self.cc_device_to = QtWidgets.QComboBox()
        #spinbox pour le montant converti
        self.spn_montant_Converti = QtWidgets.QSpinBox()
        #bonton inverser
        self.bnt_inverser = QtWidgets.QPushButton("Inverser Montant")

        #ajouter les 4 composant dans mon layout
        self.layout.addWidget(self.ccb_device_from)  
        self.layout.addWidget(self.spn_montant)
        self.layout.addWidget(self.cc_device_to)
        self.layout.addWidget(self.spn_montant_Converti)
        self.layout.addWidget(self.bnt_inverser)

    #fixer les valeur par defaut
    def SetdefaultValues(self):
        self.ccb_device_from.addItems(sorted(list(self.devise.currencies)))
        self.cc_device_to.addItems(sorted(list(self.devise.currencies)))
        #la valeur par defaut 
        self.ccb_device_from.setCurrentText("EUR")
        self.cc_device_to.setCurrentText("EUR")
        #valeur par defaut pour les spn box 
        self.spn_montant.setValue(100)
        self.spn_montant_Converti.setValue(100)
        #modifier le range pour les montant
        self.spn_montant.setRange(1,100000000)
        self.spn_montant_Converti.setRange(1,100000000)

    # programmer les event (signal) 
    def setup_connection(self):
        #pour chaque event on appelle la fonction compute
        self.ccb_device_from.activated.connect(self.compute)
        self.cc_device_to.activated.connect(self.compute)
        self.spn_montant.valueChanged.connect(self.compute)
        self.bnt_inverser.clicked.connect(self.convertir)

    def compute(self):
        """la fonction compute va récupérer les valeur modifier
        convertir le montant en appelant la methode convert() 
        elle gère le cas ou la conversion ne marche pas
        """
        devise_from = self.ccb_device_from.currentText()
        montant = self.spn_montant.value()
        devise_to = self.cc_device_to.currentText()
        try : 
            montant_converti = self.devise.convert(montant,devise_from,devise_to)
            
        except currency_converter.currency_converter.RateNotFoundError:
            print("La conversion n'a pas fonctionné.")

        else:

            self.spn_montant_Converti.setValue(montant_converti)
   
   
    def convertir(self):
        """cette methode est appelée si on clique sur le boutton inverser 
        elle va nous permettre de inverser les devise et recalculer le montant converti
        """
        device_from = self.ccb_device_from.currentText()
        device_to = self.cc_device_to.currentText()
        self.ccb_device_from.setCurrentText(device_to)
        self.cc_device_to.setCurrentText(device_from)
        self.compute()

    #modifier css de mon convertisseur
    def setup_css(self):
        self.setStyleSheet("""
        background-color :black;
        color : white;
        border: none ;
        
        """)
        self.setFixedWidth(700)
#application pour exécuter ma fenetre
app = QtWidgets.QApplication([])
#creer une fenetre
win = App()
win.show()
#executer l'application
app.exec_()