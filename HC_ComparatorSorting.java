import java.util.*;

class Player {
	String name;
	int score;

	Player(String name, int score) {
		this.name = name;
		this.score = score;
	}
}

class Checker implements Comparator<Player> {
  	// complete this method
	public int compare(Player a, Player b) {
        // compare scores of Player, the larger score is the larger Player
        int res = 0;
        if (a.score > b.score) { res = 1; }
        else if (a.score < b.score) { res = -1; }
        // if same score, compare by name
        else {
            if (a.name.compareToIgnoreCase(b.name) > 0) { res = 1; }
            if (a.name.compareToIgnoreCase(b.name) < 0) { res = -1; }
            else { res = 0; }
        }
        return res;
    }
}

/*
 * class Checker implements Comparator<Player> {
  	// complete this method
	public int compare(Player a, Player b) {
        int comparing = Integer.compare(a.score, b.score);
        if(comparing != 0)
            return comparing * -1;
        return a.name.compareTo(b.name);
    }
}
 */

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        Player[] player = new Player[n];
        Checker checker = new Checker();
        
        for(int i = 0; i < n; i++){
            player[i] = new Player(scan.next(), scan.nextInt());
        }
        scan.close();

        Arrays.sort(player, checker);
        for(int i = 0; i < player.length; i++){
            System.out.printf("%s %s\n", player[i].name, player[i].score);
        }
    }
}