# Skills Test
from pyscript import document

elements = {
    'H': {
        'Element Name': 'Hydrogen',
        'Atomic Number': '1',
        'Atomic Mass': '1.008'
    },

    'He': {
        'Element Name': 'Helium',
        'Atomic Number': '2',
        'Atomic Mass': '4.003'
    },

    'C': {
        'Element Name': 'Carbon',
        'Atomic Number': '6',
        'Atomic Mass': '12.011'
    },

    'N': {
        'Element Name': 'Nitrogen',
        'Atomic Number': '7',
        'Atomic Mass': '14.007'
    },

    'O': {
        'Element Name': 'Oxygen',
        'Atomic Number': '8',
        'Atomic Mass': '15.999'
    },

    'F': {
        'Element Name': 'Fluorine',
        'Atomic Number': '9',
        'Atomic Mass': '18.998'
    },

    'Ne': {
        'Element Name': 'Neon',
        'Atomic Number': '10',
        'Atomic Mass': '20.180'
    },

    'P': {
        'Element Name': 'Phosphorus',
        'Atomic Number': '15',
        'Atomic Mass': '30.974'
    },

    'S': {
        'Element Name': 'Sulfur',
        'Atomic Number': '16',
        'Atomic Mass': '32.07'
    },

    'Cl': {
        'Element Name': 'Chlorine',
        'Atomic Number': '17',
        'Atomic Mass': '35.45'
    },

    'Ar': {
        'Element Name': 'Argon',
        'Atomic Number': '18',
        'Atomic Mass': '39.9'
    },

    'Se': {
        'Element Name': 'Selenium',
        'Atomic Number': '34',
        'Atomic Mass': '78.971'
    },

    'Br': {
        'Element Name': 'Bromine',
        'Atomic Number': '35',
        'Atomic Mass': '79.904'
    },

    'Kr': {
        'Element Name': 'Krypton',
        'Atomic Number': '36',
        'Atomic Mass': '83.798'
    },

    'I': {
        'Element Name': 'Iodine',
        'Atomic Number': '53',
        'Atomic Mass': '126.904'
    },

    'Xe': {
        'Element Name': 'Xenon',
        'Atomic Number': '54',
        'Atomic Mass': '131.293'
    },

    'Rn': {
        'Element Name': 'Radon',
        'Atomic Number': '86',
        'Atomic Mass': 'approximately 222'
    }
}

not_found_msg = {
    'Element Name': 'Element does not exist in the non-metals list.',
    'Atomic Number': 'N/A',
    'Atomic Mass': 'N/A'
}

def element_details(e):
    symbol = document.getElementById("symbol").value.strip().capitalize()
    element = elements.get(symbol, not_found_msg)
    output = document.getElementById("output")

    output.innerHTML = f"""
        <p>Element Name: {element['Element Name']}</p>
        <p>Element Symbol: {symbol}</p>
        <p>Atomic Number: {element['Atomic Number']}</p>
        <p>Atomic Mass: {element['Atomic Mass']}</p>
    """
