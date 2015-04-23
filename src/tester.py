import PIL
import numpy as np

#landing prediction algorithm
import core

examples = ["../resources/roughness/terrainS0C0R10_100","../resources/slope_roughness/terrainS4C0R10_100","../resources/slope_roughness_craters/terrainS4C4R10_100","../resources/slope_roughness_craters_increased/terrainS4C4R20_100"]

size = 500

def main():
    #print command line arguments
    #if len(sys.argv) == 1:
    #    print("Please enter test case")
    #    sys.exit()

    #print(sys.argv[1])

    for example_num in range(len(examples)):
        
        prediction_matrix = None #core.main(examples[example_num] + "_500by500.ply")
        
        solution_path = examples[example_num] + ".invHazard.pgm"
        print(solution_path)
        solution = load_pgm_file(solution_path.replace("/", "\\"));
        
        correct = 0;
        total = size * size;
        
        for i in range(size):
            for j in range(size):
                if(solution.getpixel((i,j))==prediction_matrix[i][j]):
                    correct = correct + 1
                    
        print("The prediction accuracy is "+correct/float(total)+"%")
        
def load_pgm_file(file_name):
    with open(file_name, 'r') as infile:
        header = infile.readline()
        #width, height, maxval = [int(item) for item in header.split()[1:]]
        print(np.fromfile(infile, dtype=np.uint16).shape)
        solution = np.fromfile(infile, dtype=np.uint16).reshape((500, 500))  
        return solution
    
if __name__ == "__main__":
    main()
