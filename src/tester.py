import Image
import sys

#landing prediction algorithm
from detect import predict

resource_dir = "../resources"

test_dirs = ["/roughness/terrainS0C0R10_100.invHazard.pgm","/slope_roughness/terrainS4C0R10_100.invHazard.pgm","/slope_roughness_craters/terrainS4C4R10_100.invHazard.pgm","/slope_roughness_craters_increased/terrainS4C4R20_100.invHazard.pgm"]

size = 500

def main():
    #print command line arguments
    if len(sys.argv) == 1:
        print "Please enter test case"
        sys.exit()

    print sys.argv[1]

    solution_path = resource_dir + test_dirs[sys.argv[1]]
    solution = Image.open(solution_path);

    prediction_matrix = predict()
    
    correct = 0;
    total = size * size;
    
    for i in range(size):
        for j in range(size):
            if(solution.getpixel((i,j))==prediction_matrix[i][j]):
                correct = correct + 1
                
    print "The prediction accuracy is "+correct/float(total)+"%"
    
if __name__ == "__main__":
    main()
