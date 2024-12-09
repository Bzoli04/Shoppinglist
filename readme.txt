app.py és index.html
Főoldal: Látod a listád tartalmát.
Hozzáadás: Új dolgokat tudsz a listához adni.
Törlés: Kitörölhetsz elemeket a listából.
Minden működik pár kattintással, és az adatok csak a program futása alatt vannak megjegyezve
A weboldal megnyítása az app.py lefuttatásakor lehetséges és a terminálban lévő linkre kell kattintani

test_app.py
test_home_page: Ellenőrzi, hogy a főoldal betöltődik, és tartalmazza a "Shopping List" szöveget.

test_add_item: Teszteli, hogy egy új elem ("Milk") hozzáadható-e a bevásárlólistához, és megjelenik az oldalon.

test_delete_item: Teszteli, hogy egy elem ("Bread") törölhető-e a listából, és hogy az eltűnik az oldalról.

Ez biztosítja, hogy az alkalmazás hozzáadás, törlés és megjelenítés funkciói helyesen működnek.

test_unit.py
Ez a kód az alkalmazás logikájának részletes egységtesztjeit tartalmazza:

test_add_item_unit:

Törli az előző listaelemeket.
Hozzáad egy elemet ("apple") a listához.
Ellenőrzi, hogy az elem bekerült-e, és a lista hossza megfelelő-e.
test_delete_item_unit:

Törli az előző listaelemeket.
Hozzáad egy elemet ("Banana"), majd törli azt.
Ellenőrzi, hogy a lista üres, és az elem nincs már benne.
test_add_empty_item_unit:

Törli az előző listaelemeket.
Megakadályozza, hogy egy üres elem bekerüljön a listába.
Ellenőrzi, hogy az üres elem nem került a listába.
test_delete_nonexistent_item_unit:

Törli az előző listaelemeket.
Hozzáad egy elemet ("milk"), majd megpróbál törölni egy nem létező elemet ("egg").
Ellenőrzi, hogy a lista változatlan, és a törölni kívánt nem létező elem nem okozott hibát.
Ez a tesztcsomag a lista hozzáadás és törlés alapvető logikáját, valamint az érvényességi feltételeket (pl. üres elem, nem létező elem) ellenőrzi, és biztosítja, hogy a kód hiba nélkül működjön ilyen esetekben is.