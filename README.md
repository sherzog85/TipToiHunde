# TipToiDog
## Was ist dieses Projekt?
Meine 5-jährige Tochter spielt sehr gerne das Quiz [Wer kennt alle Hunde](https://www.laurencekingverlag.de/produkt/wer-kennt-alle-hunde/). Dabei interessiert sie sich gar nicht so sehr für die Details auf der Rückseite der Quizkarten, sondern hauptsächlich für die Hundenamen. Da sie aber noch nicht lesen kann, kann sie das Quiz nicht alleine machen. Da kam mir die Idee, den TipToi-Stift von Ravensburger dafür einzusetzen, dass sie das Spiel doch alleine spielen kann. Der Stift sollte
also die jeweiligen Hundenamen vorlesen. Ich war zuversichtlich, dass es bestimmt paar clevere Leute gibt, die herausgefunden haben, wie man
den Stift auch für eigene Projekt einsetzen kann. Und siehe da: Es gibt das geniale Tool [tttool](https://tttool.readthedocs.io/de/latest/vorwort.html). Hiermit
konnte ich das Projekt in ca. einem Tag umsetzen. Desweiteren war noch ein bisschen Python-Coding notwendig.

## Wie funktioniert der TipToi-Stift überhaupt?
Dies wird [hier](https://tttool.readthedocs.io/de/latest/konzepte.html#wie-funktioniert-der-stift) hervorragend beschrieben und daher erlaube ich mir die Faulheit,
die Funktionsweise nicht näher zu erläutern. Es sei nur so viel gesagt:
Der Stift arbeitet optisch und erkennt so genannte OID-Codes. Jeder Hundename muss nun also einem OID-Code zu geordnet werden und dann jedem OID-Code noch
eine entsprechende Audio-Datei, die den Hundenamen enthält.

## Welche Dateien sind für was?
Wenn ihr direkt damit loslegen wollt, das Quiz um die TipToi-Funktion zu erweitern, so braucht ihr lediglich 2 Dateien:
* dogs.gme: Diese Datei enthält alle Sounddateien und die notwendigen Information für den TipToi, um das Hundequiz auf diesem zu spielen. [Hier](https://tttool.readthedocs.io/de/latest/konzepte.html#was-steckt-in-einer-gme-datei)
könnt ihr genauer nachlesen, wenn ihr das Konzept der gme-Datei genauer verstehen wollt. Diese Datei könnt ihr direkt auf den Stift schieben.
* dogs_box.pdf: In dieser Datei sind die Steuerfelder und alle Hunde-Namen in OID-Code abgebildet, wobei in jedem Codefeld ein Knochen eingebettet ist. Diese Datei
muss ausgedruckt werden und dann jeder Knochen auf das entsprechende Hundekarte geklebt werden. Beim Drucken liegt leider der Teufel im Detail, [siehe auch hier](https://github.com/entropia/tip-toi-reveng/wiki/Printing).
Ich habe es mit meinem Drucker (Brother HL-L2370DN) mit den folgenden Druckeinstellungen gut hinbekommen:
  * Auflösung: HQ1200
  * Druckeinstellungen: Manuell
    * Helligkeit: 0
    * Konstrast: +34
    * Grafikqualität: Text
    * Rest wie vorgegeben
Auf weiße Etiketten spricht mein TipToi hervorragend an. Allerdings hatte ich den Ehrgeiz die Knochen auf transparente Etiketten zu drucken. Das klappt zwar immer noch, aber nicht mehr ganz so gut.
Achtung: Der Druck darf nicht skaliert werden!

Wenn ihr das Projekt modifizieren wollt, also vielleicht die Audiodateien verändern wollt, weil sie euch nicht gefallen, oder ihr eigene Hundekarten ergänzen wollt, braucht
ihr folgende Dateien, wobei die Reihenfolge, in der ich sie hier nennen, einen gewissen Ablauf beschreibt.
* dogs.xls: Diese Excel-Tabelle enthält drei Spalten: 
  1. Der Hundename in exakter Schreibweise 
  2. Ein Dateiname (ohne Leerzeichen), der den Hundenamen repräsentiert. 
  3. Die Sprache (repräsentiert durch ein Kürzel), in der später die Audio-Datei für den Hundenamen generiert werden soll
* gen_dogs.py: Dieses Skript lädt diese Excel-Datei ein und lässt eine Schleife über alle Hundenamen laufen. Hierbei wird mit Hilfe der _Google Text-to-Speech_-API 
eine Audiodatei für jeden Hundenamen erzeugt. Desweiteren wird eine entsprechende yaml-Datei erzeugt. Diese Datei benötigt das tttool dann später um zu wissen für welche Ereignisse/Begriffe
(hier: die Hundename) welche Aktionen (hier: Abspielen des Hundenamens) generiert und OID codiert werden sollen.
* hello_dog.ogg: Diese ist eine akustische Begrüßung, die ich eingespielt habe und die ertönt, wenn das Start-Symbol gewählt wird. Sie kann nach Belieben durch eine andere Datei ersetzt werden. Eure Kinder freuen sich bestimmt, wenn sie eure eigene Stimme zu hören bekommen. 
* gen_gme.bat: Dieses Batch-Skript erzeugt aus der yaml-Datei und den Soundfiles die entsprechende gme-Datei
* gen_oid.bat: Dieses Batch-Skript erzeugt die OID-Codes in einer Tabelle im PDF-Format. Die Größe habe ich entsprechend so gewählt, dass der Knochen auf der Quizkarte nicht zu viel Platz einnimmt. Außerdem habe ich die Pixel-Größe auf 3 (statt wie standardmäßig 2) eingestellt. Dadurch hat mein Stift die Codes überhaupt erst erkannt.
* overlay.docx: In diesem Word-Dokument sind Hundeknochen tabellarisch im gleichen Raster angeordnet, wie die OID-Codes in dem PDF, was durch das vorherige Skript erstellt worden ist. Daraus muss eine PDF-Datei erstellt werden (auch hier nicht skalieren!)
* merge_pdf.py: Dieses Python-Skript verschmelzt die dogs.pdf mit der overlay.pdf zu dogs_box.pdf, die dann gemäß obiger Beschreibung ausgedruckt werden kann.

Viel Spaß beim Verwenden und Modifizieren!
Über eine Rückmeldung, wenn ihr es erfolgreich umgesetzt habt, würde ich mich freuen!
