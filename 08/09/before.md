# Kvíz před cvičením (#9)

Kvíz musí být nahrán do GitLabu před začátkem vašeho cvičení.

Každá otázka je za 25 bodů.

Vaši odpověď vložte do označeného bloku (místo tří teček).



## Otázka Q1

Stručně napište, co pro vás bylo nejnáročnější na předchozím cvičení.


Vaše odpověď: **[A1]** regex sám o sebe pomerne dáva zmysel ale dlho mi trvalo kým som pochopil ako skombinovať výrazy na to aby som dosiahol čo chcem **[/A1]**



## Otázka Q2

Stručně porovnejte, proč `passwd` má nastavený set-uid bit, ale
`dnf` (nebo `apt`) jsou spouštěny skrze `sudo` (a nikdy nemají
set-uid bit nastavený).

Vzpomeňte si, že `passwd` slouží ke změně hesla (má i jiné funkce,
ale ty můžeme teď ignorovat).

`dnf` a `apt` jsou příklady správců balíčků, tj. softwaru, který
se stará o instalaci aplikací do systému.

Vaše odpověď: **[A2]** podľa manpages príkaz passwd mení heslo uživateľa čo je z hladiska, bezpečnosti operácia ktorá by si mala vždy vyžadovať zvýšené práva na druhej strane od takého package managera môžeme chcieť aby nám ukázal nainštalované aplikácie...to je pomerne neškodná operácia, teda v skratke apt nepotrebuje mať zvýšené privilégia na každý príkaz preto nemá nastavený set-uid bit **[/A2]**



## Otázka Q3

Vyberte všechna pravdivá tvrzení o správě balíčků.

1. Správce balíčků je hlavní prvkem, který se stará o instalaci
   softwaru na Linuxovém systému.
2. Správce balíčků se používá ke spuštění nainstalovaných programů.
3. Softwarový repozitář vždy obsahuje jen nepatentovaný software.
4. Softwarový repozitář může být připraven (nastaven) jen správci distribuce.
5. Balíčky obvykle obsahují samostatný program (např. prohlížeč Firefox)
   nebo sadu souvisejících programů (např. kancelářský balík).

Vaše odpověď: **[A3]** 1,5 **[/A3]**



## Otázka Q4

Vyberte všechna pravdivá tvrzení o signálech a procesech.

1. Signál je asynchronní komunikační kanál.
2. Aplikace může na libovolný signál zareagovat podle svého uvážení.
3. Signály jsou rozlišeny jen jejich číslem.
4. Některé signály nejsou aplikaci nikdy doručeny (tj. jsou zpracovány
   jen kernelem).
5. Aplikace musí skončit do 5 sekund od obdržení signálu `TERM`
   (a to za všech okolností).
6. Proces reprezentuje běžící program.
7. Každý proces má svůj vlastní spustitelný soubor, ze kterého byl spuštěn
   (jinými slovy, existuje mapování 1:1 mezi procesy a spustitelnými soubory).
8. Každý proces má unikátní ID, nazývané PID.

Vaše odpověď: **[A4]** 1,3,4,6,8 **[/A4]**



