package botbeta;


import java.util.HashMap;

public class PlayerInfo {
	public static HashMap<String, Integer> player = new HashMap<String, Integer>();
	
	public static boolean setPlayer(String tag) {
		if(!player.containsKey(tag)) {
			player.put(tag, 100000);
			return true;
		}
		else {
			return false;
		}
	}
	
	public static int getPoint(String tag) {
		return player.get(tag);
	}
	
	public static boolean contain(String tag) {
		return player.containsKey(tag);
	}
	
	public static void addPoint(String tag, int p) {
		player.put(tag, getPoint(tag) + p);
	}
}