PORTB = $6000
PORTA = $6001
DDRB = $6002
DDRA = $6003

E = %10000000
RW = %01000000
RS = %00100000

  .org $8000
  
reset:
  lda #$ff       ; Set all pins on PORT B to output
  sta DDRB

  lda #%11100000 ; Sets top three pins on PORT A to output
  sta DDRA
  
  lda #%00111000 ; Set 8-bit mode; 2-line display; 5 x 8 font
  sta PORTB

  lda #0         ; Clears Enable, Register Select, and Read Write bits
  sta PORTA

  lda #E         ; Turns on Enable bit to allow display to accept instruction
  sta PORTA

  lda #0         ; Clears E/RS/RW bits
  sta PORTA

  lda #%00001110 ; Turns display on; Enables cursor; turns off cursor blinking
  sta PORTB

  lda #0         ; Clears E/RS/RW bits
  sta PORTA

  lda #E         ; Turns on Enable bit to allow display to accept instruction
  sta PORTA

  lda #0         ; Clears E/RS/RW bits
  sta PORTA

  lda #%00000110 ; Increments characters; display is static and does not scroll
  sta PORTB

  lda #0         ; Clears E/RS/RW bits
  sta PORTA

  lda #E         ; Turns on Enable bit to allow display to accept instruction
  sta PORTA

  lda #0         ; Clears E/RS/RW bits
  sta PORTA

  lda #"H"      ; Loads an H into port B to be displayed
  sta PORTB
  lda #RS        ; Turns on Register select pin
  sta PORTA
  lda #(RS | E)  ; Turns on Enable bit and Register select to send character
  sta PORTA
  lda #RS        ; Turns on Register select pin
  sta PORTA

  lda #"e"      ; Loads an H into port B to be displayed
  sta PORTB
  lda #RS        ; Turns on Register select pin
  sta PORTA
  lda #(RS | E)  ; Turns on Enable bit and Register select to send character
  sta PORTA
  lda #RS        ; Turns on Register select pin
  sta PORTA

  lda #"l"      ; Loads an H into port B to be displayed
  sta PORTB
  lda #RS        ; Turns on Register select pin
  sta PORTA
  lda #(RS | E)  ; Turns on Enable bit and Register select to send character
  sta PORTA
  lda #RS        ; Turns on Register select pin
  sta PORTA

  lda #"l"      ; Loads an H into port B to be displayed
  sta PORTB
  lda #RS        ; Turns on Register select pin
  sta PORTA
  lda #(RS | E)  ; Turns on Enable bit and Register select to send character
  sta PORTA
  lda #RS        ; Turns on Register select pin
  sta PORTA

  lda #"o"      ; Loads an H into port B to be displayed
  sta PORTB
  lda #RS        ; Turns on Register select pin
  sta PORTA
  lda #(RS | E)  ; Turns on Enable bit and Register select to send character
  sta PORTA
  lda #RS        ; Turns on Register select pin
  sta PORTA

  lda #" "      ; Loads an H into port B to be displayed
  sta PORTB
  lda #RS        ; Turns on Register select pin
  sta PORTA
  lda #(RS | E)  ; Turns on Enable bit and Register select to send character
  sta PORTA
  lda #RS        ; Turns on Register select pin
  sta PORTA

  lda #"W"      ; Loads an H into port B to be displayed
  sta PORTB
  lda #RS        ; Turns on Register select pin
  sta PORTA
  lda #(RS | E)  ; Turns on Enable bit and Register select to send character
  sta PORTA
  lda #RS        ; Turns on Register select pin
  sta PORTA

  lda #"o"      ; Loads an H into port B to be displayed
  sta PORTB
  lda #RS        ; Turns on Register select pin
  sta PORTA
  lda #(RS | E)  ; Turns on Enable bit and Register select to send character
  sta PORTA
  lda #RS        ; Turns on Register select pin
  sta PORTA

  lda #"r"      ; Loads an H into port B to be displayed
  sta PORTB
  lda #RS        ; Turns on Register select pin
  sta PORTA
  lda #(RS | E)  ; Turns on Enable bit and Register select to send character
  sta PORTA
  lda #RS        ; Turns on Register select pin
  sta PORTA

  lda #"l"      ; Loads an H into port B to be displayed
  sta PORTB
  lda #RS        ; Turns on Register select pin
  sta PORTA
  lda #(RS | E)  ; Turns on Enable bit and Register select to send character
  sta PORTA
  lda #RS        ; Turns on Register select pin
  sta PORTA

  lda #"d"      ; Loads an H into port B to be displayed
  sta PORTB
  lda #RS        ; Turns on Register select pin
  sta PORTA
  lda #(RS | E)  ; Turns on Enable bit and Register select to send character
  sta PORTA
  lda #RS        ; Turns on Register select pin
  sta PORTA

  lda #"!"      ; Loads an H into port B to be displayed
  sta PORTB
  lda #RS        ; Turns on Register select pin
  sta PORTA
  lda #(RS | E)  ; Turns on Enable bit and Register select to send character
  sta PORTA
  lda #RS        ; Turns on Register select pin
  sta PORTA

loop:
  jmp loop

  .org $fffc
  .word reset
  .word $0000
