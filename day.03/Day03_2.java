import java.util.Scanner;

class Day03_2 {
    static class Job {
        public final int id;
        public final int left;
        public final int top;
        public final int width;
        public final int height;

        public Job(int id, int left, int top, int width, int height) {
            this.id = id;
            this.left = left;
            this.top = top;
            this.width = width;
            this.height = height;
        }

        public String toString() {
            return "id: " + id + ", left: " + left + ", top: " + top
                + ", width: " + width + ", height: " + height;
        }
    }

    private static Job parseJob(String line) {
        String[] parts = line.split(" ");
            
        int i = Integer.parseInt(parts[0].substring(1));
            
        String[] pos = parts[2].split(",");
        String[] sz = parts[3].split("x");

        int l = Integer.parseInt(pos[0]);
        int t = Integer.parseInt(pos[1].substring(0, pos[1].length() - 1));
        int w = Integer.parseInt(sz[0]);
        int h = Integer.parseInt(sz[1]);

        return new Job(i, l, t, w, h);
    }

    public static void main(String[] args) {
        int[][] arr = new int[1000][1000];
        boolean[] hasOverlap = new boolean[1234];

        Scanner sc = new Scanner(System.in);
        while (sc.hasNextLine()) {
            Job job = parseJob(sc.nextLine());

            for (int y = job.top; y < job.top + job.height; y++) {
                for (int x = job.left; x < job.left + job.width; x++) {
                    if (arr[y][x] == 0) {
                        arr[y][x] = job.id;
                    } else {
                        hasOverlap[job.id] = true;
                        hasOverlap[arr[y][x]] = true;
                    }
                }
            }
        }

        for (int i = 1; i < hasOverlap.length; i++) {
            if (!hasOverlap[i]) {
                System.out.println(i);
                return;
            }
        }
    }
}
