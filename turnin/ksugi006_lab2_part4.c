/*	Author: ksugi006
 *  Partner(s) Name: 
 *	Lab Section:
 *	Assignment: Lab 2  Exercise 2
 *	Exercise Description: [optional - include for your own benefit]
 *
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */
#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif

int main(void) {
    /* Insert DDR and PORT initializations */
	DDRA = 0x00; PORTA = 0xFF;
	DDRB = 0x00; PORTB = 0xFF;
	DDRC = 0x00; PORTC = 0x00;
	DDRD = 0xFF; PORTD = 0x00;
	
	unsigned char totWeight = 0x00;
	unsigned short difWeight = 0x00;
	unsigned char tmp = 0x00;
    /* Insert your solution below */
    while (1) {
	
	totWeight = 0;
	difWeight = 0;
	tmp = 0;

	totWeight = PINA + PINB + PINC;
	tmp  = totWeight >> 2;
	

	if(totWeight > 140){
		tmp = tmp | 0x01; //setting PD0 to 1 if > 140
	}

	difWeight = PINA - PINC;

	if((difWeight >= 80)){
		tmp = tmp | 0x02; //setting PD1 to 1 if inbetween 50 and -50
	}

	PORTD = tmp;
   }	
    return 0;
}
