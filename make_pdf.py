import sys
import nbconvert
import nbformat

Complex_Networks = [
    "leggi_pdb",
    "PCM_permute",
    "ER_networks",
    "real_net_analysis",
    "laplacian_lab_07",
]

Pattern_Recognition = [
    "Pat_Rec_Lab_1",
    "SwissRoll_PCA_MDS_LLE_IsoMap_tSNE_UMAP",
    "simple_perceptron",
    "neuron_class",
    "scikit_intro",
]

out_notebook = nbformat.v4.new_notebook()
subject = sys.argv[1].lower()
if subject == 'cn':
    files = Complex_Networks
    outfile = 'Complex_Networks'
elif subject == 'pr':
    files = Pattern_Recognition
    outfile = 'Pattern_Recognition'

for file in files:
    temp_notebook = nbformat.read('./src/{}/{}.ipynb'.format(outfile, file), as_version=4)
    out_notebook.cells.extend(temp_notebook.cells)

out_pdf = nbconvert.PDFExporter().from_notebook_node(out_notebook)[0]
with open('{}.pdf'.format(outfile), 'wb') as f:
    f.write(out_pdf)