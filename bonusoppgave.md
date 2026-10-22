# Hva er rate limiting?

Rate limiting betyr at en server bestemmer hvor mange forespørsler én bruker (eller én IP-adresse) kan sende i løpet av en viss tid, for eksempel maks 10 forespørsler per sekund. Hvis noen sender flere forespørsler enn dette, blokkerer eller avviser serveren de ekstra forespørslene.

I mitt DoS-angrep sendte jeg mange forespørsler fra samme maskin veldig raskt etter hverandre. Hvis serveren hadde rate limiting, ville den ha oppdaget at forespørslene kom altfor fort fra samme IP-adresse, og den ville ha stoppet eller forsinket de ekstra forespørslene i stedet for å svare på alle sammen.

Dette ville ha gjort angrepet mitt mye mindre effektivt, fordi serveren bare måtte håndtere et begrenset antall forespørsler fra meg, i stedet for tusenvis på kort tid.