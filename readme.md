# 4HV-Project: Game maken met Python
#### 2020 / 2021
___
### Text Adventure: The Dungeon Zone

##### Team: Vincent Speijer & Mikail Sola

##### Basisspel:

- [X] In het basisspel is het alleen noodzakelijk om van locatie naar locatie te gaan. 
- [X] De speler/avonturier mag alleen éénletterige opdrachten intikken om op avontuur te gaan. 
- [X] De letters n, e, w, s en q zijn verplicht en staan voor de vier windrichtingen en Quit (stop). 
- [X] De speler kan de commando’s zowel in hoofdletters als in kleine letters intikken.
- [X] De speler kan een naam invoeren. De naam wordt door het spel onthouden.

##### Verbeteringen:
- [X] De speler mag alleen opdrachten invoeren die niet langer of korter zijn dan 1 teken. Bij foute invoer wordt een foutbericht getoond. (max. 10 punten)
- [X] Op een locatie kunnen zich objecten bevinden die in de beschrijving van de locatie worden getoond. Tip: Gebruik een Dictionary van objecten. Elk item in de dictionary bevat de naam (of namen) van de locatie, waar het object zich in bevindt. (max. 10 punten)
- [X] Door het invoeren van de letter ‘g’ (GET) is het mogelijk een object te pakken en in de inventory van de speler te plaatsen. Het object verdwijnt uit de locatie. Met de letter ‘i’ (INVENTORY) krijg je een beschrijving van alle objecten die zich in de inventory bevinden. Met de letter ‘d’ (DROP) kan je een object laten vallen. Het object verschijnt in de locatie waar je je dan bevindt. (max. 15 punten).
  - Voor ‘g’ is er ‘p’ (Pick up) gebruikt.
- [X] Het is niet mogelijk om andere letters in te voeren dan degene die als commando gebruikt worden.  (max. 5 punten)
- [X] Je kan het spel uitspelen en/of game over gaan.

##### Eisen:
- [X] Er wordt gebruik gemaakt van commentaar in het programma.
- [X] Er wordt minimaal 1 functie gebruikt.
- [X] Er is input van de gebruiker (evt. met controle op de invoer).
- [X] Er wordt gebruik gemaakt van concatenation.
- [X] Er wordt gebruik gemaakt van string methodes.
- [X] Er wordt gebruik gemaakt van tenminste één while-loop.
- [X] Er wordt gebruik gemaakt van minstens één dictionary.
- [X] Er zijn minstens 10 locaties.

##### Extra functies:
- Events in bepaalde kamers
  - 2 Fights
  - 1 Coinflip battle
  - 1 Dance battle
- Door het invoeren van de letter ‘u’ kun je in bepaalde kamers voorwerpen gebruiken om sommige terug te krijgen of door te gaan naar een volgende kamer.
- Door het invoeren van de letter ‘m’ wordt er een map laten zien van het spel, zodat jee niet kan verdwalen.
- Door het invoeren van de letter ‘o’ is het mogelijk om de snelheid van het printen te weizigen, voor als je haast hebt.
- Door het invoeren van de letter ‘t’ wordt er extra dialogue gegeven als backstory voor de kamer of characters. In sommige kamers zitten er hints verwerkt in de extra dialogue
___

###### All code written in the files is illegal to copy without permission from any of the owners. Please refrain from stealing even parts from the code. It's much more fun to figure something out yourself anyways.
###### Mystivian™ & Leap™
###### Thanks for reading, and most likely playing!	