# Array of tests to run (in order)
# Each test contains
#   description - 
#   steps - A list of steps to perform, each step can have
#       inputs - A list of tuples for the inputs to apply at that step
#       *time - The time (in ms) to wait before continuing to the next step 
#           and before checking expected values for this step. The time should be a multiple of
#           the period of the system
#       *iterations - The number of clock ticks to wait (periods)
#       expected - The expected value at the end of this step (after the "time" has elapsed.) 
#           If this value is incorrect the test will fail early before completing.
#       * only one of these should be used
#   expected - The expected output (as a list of tuples) at the end of this test
# An example set of tests is shown below. It is important to note that these tests are not "unit tests" in 
# that they are not ran in isolation but in the order shown and the state of the device is not reset or 
# altered in between executions (unless preconditions are used).
tests = [ {'description': 'PINA: 0x00 PINB: 0x00 PINC: 0x00 => PORTC: 00000000 = 0x00',
    'steps': [ {'inputs': [('PINA',0x00), ('PINB', 0x00), ('PINC', 0x00)], 'iterations': 1 } ],
    'expected': [('PORTD',0x00)],
    },
	{'description': 'PINA = 50 PINB: 50 PINC: 50 => PORTC: 150 = 10010101 = 0x95',
	'steps': [{'inputs': [('PINA', 0x32), ('PINB', 0x32), ('PINC', 0x32)], 'iterations': 1} ],
	'expected': [('PORTD', 0x95)],
	},
        {'description': 'PINA = 90 PINB: 50 PINC: 10 => PORTC: 150 = 10010111 = 0x97',
        'steps': [{'inputs': [('PINA', 0x5A), ('PINB', 0x32), ('PINC', 0x0A)], 'iterations': 1} ],
        'expected': [('PORTD', 0x97)],
        },
        {'description': 'PINA = 40 PINB: 50 PINC: 40 => PORTC: 130 = 10000000 = 0x80',
        'steps': [{'inputs': [('PINA', 0x28), ('PINB', 0x32), ('PINC', 0x28)], 'iterations': 1} ],
        'expected': [('PORTD', 0x80)],
        },
        {'description': 'PINA = 40 PINB: 40 PINC: 40 => PORTC: 120 = 10000010 = 0x31',
        'steps': [{'inputs': [('PINA', 0x40), ('PINB', 0x40), ('PINC', 0x40)], 'iterations': 1} ],
        'expected': [('PORTD', 0x31)],
        },
]

# Optionally you can add a set of "watch" variables these need to be global or static and may need
# to be scoped at the function level (for static variables) if there are naming conflicts. The 
# variables listed here will display everytime you hit (and stop at) a breakpoint
#watch = ['<function>::<static-var>','PORTB']

