a = [{"jj": "kk"},
     {"jj": ["aa","kk"]}]

print(a)
print(a[0])
print(a.index(a[0]))

name = [
    {
    "category": "Science",
    "question": "Which                                                                                                                                                                                                                                                                                     mechanism is primarily responsible for the production of energy in a Sun-like star?",
    "choices": [
        "Nuclear fission",
        "Proton-proton chain",
        "Triple-alpha process",
        "CNO cycle"
    ],
    "answer": 2,
    "difficulty": "Impossible",
    "hint": "It converts hydrogen into helium through a sequence of nuclear reactions."
},
{
    "category": "Science",
    "question": "Which type of supernova results from the thermonuclear destruction of a carbon-oxygen white dwarf?",
    "choices": [
        "Type Ia",
        "Type Ib",
        "Type II",
        "Type IIn"
    ],
    "answer": 1,
    "difficulty": "Impossible",
    "hint": "Unlike core-collapse supernovae, this type involves a white dwarf."
},
{
    "category": "Science",
    "question": "Which phenomenon causes light from a distant galaxy to be distorted and magnified by a massive object between the galaxy and observer?",
    "choices": [
        "Gravitational lensing",
        "Compton scattering",
        "Cherenkov radiation",
        "Doppler broadening"
    ],
    "answer": 1,
    "difficulty": "Impossible",
    "hint": "Einstein's general theory of relativity predicts this effect."
},
{
    "category": "Science",
    "question": "Which discontinuity marks the boundary between Earth's crust and mantle?",
    "choices": [
        "Gutenberg discontinuity",
        "Lehmann discontinuity",
        "Mohorovičić discontinuity",
        "Wiechert discontinuity"
    ],
    "answer": 3,
    "difficulty": "Impossible",
    "hint": "Its name is commonly shortened to a three-letter abbreviation beginning with 'Mo'."
},
{
    "category": "Science",
    "question": "Which process allows bacteria to acquire DNA directly from their surrounding environment?",
    "choices": [
        "Conjugation",
        "Transformation",
        "Transduction",
        "Translation"
    ],
    "answer": 2,
    "difficulty": "Impossible",
    "hint": "Unlike conjugation, this process does not require direct cell-to-cell contact."
},
{
    "category": "Science",
    "question": "Which enzyme synthesizes the short RNA primers required during DNA replication?",
    "choices": [
        "DNA ligase",
        "Primase",
        "Helicase",
        "Topoisomerase"
    ],
    "answer": 2,
    "difficulty": "Impossible",
    "hint": "It creates the starting point from which DNA polymerase can begin synthesis."
},
{
    "category": "Science",
    "question": "Which molecular complex is responsible for catalyzing peptide-bond formation during protein synthesis?",
    "choices": [
        "Proteasome",
        "Ribosome",
        "Centrosome",
        "Spliceosome"
    ],
    "answer": 2,
    "difficulty": "Impossible",
    "hint": "It reads messenger RNA and links amino acids together."
},
{
    "category": "Science",
    "question": "Which hypothetical particle is one of the proposed candidates for dark matter?",
    "choices": [
        "WIMP",
        "Photon",
        "Gluon",
        "Positron"
    ],
    "answer": 1,
    "difficulty": "Impossible",
    "hint": "Its name is an acronym meaning Weakly Interacting Massive Particle."
},
{
    "category": "Science",
    "question": "Which theorem states that no physical information can be transmitted faster than light through quantum entanglement?",
    "choices": [
        "No-cloning theorem",
        "No-signaling theorem",
        "Spin-statistics theorem",
        "Bell's theorem"
    ],
    "answer": 2,
    "difficulty": "Impossible",
    "hint": "It concerns the inability to use entanglement alone for faster-than-light communication."
}
]
import random
duplicate=[]
for i in name:
    duplicate.append(i)
    

print(random.choice(duplicate))



