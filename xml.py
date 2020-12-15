import xml.dom.minidom
plik = xml.dom.minidom.parse("pracownicy.xml")


new = plik.createElement("Pracownik")
new.setAttribute("Rok urodzenia", "1998")
new.setAttribute("Miasto", "Krakow")
plik.firstChild.appendChild(new)
xml_string = plik.toxml()
save_path_file = "pracownicy_update.xml"

with open(save_path_file, "w") as f: 
    f.write(xml_string)  

    