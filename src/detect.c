#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<assert.h>

int COLS = 500;
int ROWS = 500;

static void rev_float(float *longone)
{
	struct long_bytes {
		char byte1;
		char byte2;
		char byte3;
		char byte4;
	} *longptr;
	unsigned char temp;
 
	longptr = (struct long_bytes *) longone;
	temp = longptr->byte1;
	longptr->byte1 = longptr->byte4;
	longptr->byte4 = temp;
	temp = longptr->byte2;
	longptr->byte2 = longptr->byte3;
	longptr->byte3 = temp;
}

float* read_dem(char *filename)
{
	float *dem;
	int cols, rows;
	int i;
	FILE *fp;
	cols = 500;
	rows = 500;
	dem = (float *)malloc(sizeof(float)*cols*rows);
	fp = fopen(filename, "rb");
	fread(dem, sizeof(float), cols*rows, fp);

	for(i = 0; i < cols*rows; ++i)
	{
		rev_float(&dem[i]);
	}

	fclose(fp);
	return dem;
}

int incline_within_thresh(float thresh, float del_x, float del_y)
{
	float div = del_y/del_x;
	float ang = atan(div);
	return ang < thresh;
}

float get_in(float* surf, int x, int y)
{
	return surf[x+ROWS*y];
}

int rover_pad_level(float* surf, int pad_x, int pad_y)
{
	// Make sure we can load surrounding values
	assert(pad_x>0);
	assert(pad_y>0);
	assert(pad_x<ROWS);
	assert(pad_y<COLS);

	float THRESH = 0.001;

	float mid = get_in(surf,pad_x,pad_y);
	float n = get_in(surf,pad_x,pad_y - 1) - mid;
	float s = get_in(surf,pad_x,pad_y + 1) - mid;
	float e = get_in(surf,pad_x - 1,pad_y) - mid;
	float w = get_in(surf,pad_x + 1,pad_y) - mid;

	int nb = THRESH > n;
	int sb = THRESH > s;
	int eb = THRESH > e;
	int wb = THRESH > w;
	
	return nb && sb && eb && wb;
}

int rover_pads_alligned(float p1, float p2, float p3, float p4)
{
	float thresh = 0.174532925; //10 degrees in radians
	return 0;
}


int main(int argc, char *argv[])
{
	char* file_name = argv[1];
	/* float (*surface) [500] = (float (*)[500]) read_dem(file_name); */
	/* smap* surface = (smap*)((float (*)[500]) read_dem(file_name)); */
	float* surf  = read_dem(file_name);
	/* print_submatrix(surface,0,60,10,10); */
	return 0;
}
