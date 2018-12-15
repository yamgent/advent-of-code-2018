import java.util.Scanner;
import java.util.ArrayList;

class Day06_1 {
    /*
    static class Box {
        public int left;
        public int right;
        public int top;
        public int bottom;

        public Box(int left, int right, int top, int bottom) {
            this.left = left;
            this.right = right;
            this.top = top;
            this.bottom = bottom;
        }
    }
    */

    static class Point {
        public int x;
        public int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
        public int dist(Point other) {
            return Math.abs(other.x - x) + Math.abs(other.y - y);
        }

        /*
        public boolean onBorder(Box border) {
            return border.left == x || border.right == x || 
                border.top == y || border.bottom == y;
        }
        */
    }

    /*
    private static Box findBoundingBox(ArrayList<Point> points) {
        Point first = points.get(0);
        Box result = new Box(first.x, first.x, first.y, first.y);

        for (Point p : points) {
            result.left = Math.min(result.left, p.x);
            result.right = Math.max(result.right, p.x);
            result.top = Math.min(result.top, p.y);
            result.bottom = Math.max(result.bottom, p.y);
        }

        return result;
    }
    */

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Point> points = new ArrayList<Point>();

        while (sc.hasNextLine()) {
            String[] line = sc.nextLine().split(",");
            points.add(new Point(Integer.parseInt(line[0]), Integer.parseInt(line[1].trim())));
        }

        // Box boundingBox = findBoundingBox(points);
        int[] pointsArea = new int[points.size()];
        boolean[] isInfinite = new boolean[points.size()];

        for (int y = 0; y < 1000; y++) {
            for (int x = 0; x < 1000; x++) {
                int nearestPoint = -1;
                int nearestSoFar = 9999;
                Point current = new Point(x, y);

                for (int p = 0; p < points.size(); p++) {
                    int dist = current.dist(points.get(p));

                    if (dist == nearestSoFar) {
                        nearestPoint = -1;  // multiple location
                    } else if (dist < nearestSoFar) {
                        nearestPoint = p;
                        nearestSoFar = dist;
                    }
                }

                if (nearestPoint != -1) {
                    pointsArea[nearestPoint]++;

                    // touch boundary = assume is infinite
                    if (x == 0 || y == 0 || x == 999 || y == 999) {
                        isInfinite[nearestPoint] = true;
                    }
                }

                /*
                if (nearestPoint == -1) {
                    System.out.print("..");
                } else if (nearestSoFar == 0) {
                    System.out.print("**");
                } else {
                    System.out.printf("%02d", nearestPoint);
                }
                */
            }
            /*
            System.out.println();
            */
        }



        int largestArea = 0;
        for (int p = 0; p < points.size(); p++) {
            if (!isInfinite[p]) {
                largestArea = Math.max(largestArea, pointsArea[p]);
            }
        }

        System.out.println(largestArea);
    }
}
