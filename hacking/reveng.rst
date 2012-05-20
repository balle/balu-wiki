####################
Reverse Engineering
####################

2 byte = 1 word
4 byte = 1 dword

ebx = base pointer (e.g. array start)
ecx = counter register
edx = data register
esi = source register
edi = destination register

z-flag - zero flag (is zero is last result was zero)
cf / of - overflow flags
sign flag - indicated if integer is signed or unsigned

wenn zwei gleiche zahlen mit cmp verglichen werden wird z-flag gesetzt wenn beide gleich sind, wenn die erste zahl kleiner als die zweite ist, ist s-flag 1 (bei signed, bei unsigned ist c-flag 1), wenn beide 0 sind ist die erste zahl größer

test = AND (setzt z-flag auf 1 wenn src und dst gleich sind)
xor mit zwei gleichen registern schreibt 0 in das register

adressen >= 0x80000000 sind kernel address space

jeder prozess hat mindestens einen thread (es gibt kein fork unter windows)
jeder thread hat 2 stacks einen für user und einen für kernel mode, denn ein thread wird via kernel syscalls in den priviledged mode geschaltet

prozess initialisierung:
1. CreateProcess legt ein neues Process Object im Kernel an, mapped die EXE + NTDLL.DLL ins RAM, startet einen thread und allokiert stack space
LdrpInitialize (NTDLL.DLL) liest import tables und lädt alle DLLs nach
dann wird BaseProcessStart (KERNEL32.DLL) aufgerufen -> startet WinMain

dos header (beinhaltet ein dos programm das ausgibt, dass das programm nicht unter dos läuft) ein zusätzlicher eintrag (e_lfanew) zeigt auf den wirklichen pe header

die struktur eines PE binary auf der platte ist die selbe wie im ram d.h. wenn man etwas interessantes in der datei gefunden hat ist es an der selben virtuellen adresse im ram

sectionheader ist normalerweise zwischen imagebase start und imagebase + 1000
imagebase bekommt man via getmodulehandlea

die adresse im pe header sind alle relativ zur imagebase (und "verkehrt herum" sprich lil endian)

es gibt eine section pro importierter dll und jede section hat eine imported address table (IAT)
IAT mapped die dll function adresse auf die virtuelle adresse im ram (wie GOT section im ELF header)

directories sind optionale header mit denen ein PE executable erweitert werden kann z.b. import / export table,
- resource table (hier werden bilder und statische strings referenziert),
- base relocation table (beinhaltet eine liste von adressen, die neuberechnet werden müssen),
- thread local storage table (enthält eine section die privat für den aktuellen thread ist)

wenn eine exception auftrifft ruft der kernel alle functionen aus der exception handler list (in der thread informaion block section) auf und jede funktion entscheidet dann selbst ob sie sich um die exception kümmert oder nicht

KERNEL32.DLL beinhaltet I/O, memory- process- und thread management
GDI32.DLL deckt alle low-level gui dienste ab wie linien zeichnen
USER32.DLL implementiert alle GUI dienste wie menus, dialoge, window-management etc

switching to kernel mode
vor windows2000 wurde die syscall nr in eax geladend und int 2e aufgerufen
jetzt wird dieser aufruf hinter dem befehl sysenter versteckt ( wird immer nur via SystemCallStub aufgerufen weil sysenter selbst sich nicht den stackpointer merkt)


