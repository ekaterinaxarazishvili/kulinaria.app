from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("kulinariaaa.ui", self)

        self.pushButton.clicked.connect(self.show_recipe)

        self.recipes = {
            "ცეზარი": "ინგრედიენტები:\n- სალათის ფურცელი\n- პარმეზანის ყველი\n- ქათმის ფილე\n- მსუხარი\n- ცეზარის სოუსი\n- პომიდორი",
            "ბორში": "ინგრედიენტები:\n- ჭარხალი\n- კარტოფილი\n- ხახვი\n- სტაფილო\n- ხორცი\n- კომბოსტო\n- ნიახური,პეტრუშკა,დაფნა\n- ხახვი",
            "ჩაქაფული": "ინგრედიენტები:\n- ძროხის ხორცი\n- ნედლი ხახვი\n- ტარხუნა,წიწმატი,კინძი,პეტრუშკა\n- რქაწითელი 2 ჭიქა\n- ცხარე წიწაკა\n- მარილი\n- ტყემალი",
            "მარწყვის ტორტი": "ინგრედიენტები:\n- მარწყვი\n- ფქვილი\n- კარაქი\n- შაქარი\n- კვერცხი\n- ვანილი\n- ნაღები"
        }

    def show_recipe(self):

        if self.radioButton.isChecked():
            recipe = "ცეზარი"
        elif self.radioButton_2.isChecked():
            recipe = "ბორში"
        elif self.radioButton_3.isChecked():
            recipe = "ჩაქაფული"
        elif self.radioButton_4.isChecked():
            recipe = "მარწყვის ტორტი"
        else:
            self.label_2.setText("გთხოვთ აირჩიოთ რეცეპტი!")
            return

        self.label_2.setText(self.recipes.get(recipe, "რეცეპტი ვერ მოიძებნა"))


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()