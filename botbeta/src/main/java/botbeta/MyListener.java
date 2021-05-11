package botbeta;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Map.Entry;

import net.dv8tion.jda.api.entities.TextChannel;
import net.dv8tion.jda.api.entities.User;
import net.dv8tion.jda.api.events.message.MessageReceivedEvent;
import net.dv8tion.jda.api.hooks.ListenerAdapter;

public class MyListener extends ListenerAdapter {
	String prefix = "!";

	@Override
	public void onMessageReceived(MessageReceivedEvent e) {
		User user = e.getAuthor();
		TextChannel channel = e.getTextChannel();
		String msg = e.getMessage().getContentRaw();
		String tag = user.getAsTag();

		if (user.isBot()) {
			return;
		}

		if (msg.equals("!설명")) {
			channel.sendMessage("" + "-도박장에 오신걸 환영합니다!:D-\n" + "\n" + "이 봇은 현재 테스트중에 있으며 게임은 차차 추가 될 예정입니다.\n" + "\n"
					+ "-게임 룰-\n" + "\n" + "-홀짝 게임:홀 또는 짝을 선택하여 참가합니다.(승리시 잔액의 50% 추가 획득, 패배시 잔액의 20%손실)\n" + "\n" + "*-명령어 목록-*\n"
					+ "\n" + "!도박참여:도박에 참가합니다. 이 명령어를 사용해야 게임을 즐길 수 있습니다.\n"
					+ "!잔액:현재 남은 잔액을 확인합니다. 잔액이 높을수록 게임의 부담이 높아지지만 랭킹에 오를 수 있습니다.\n" + "!홀짝 홀:홀짝게임에 홀을 걸고 참가합니다.\n"
					+ "!홀짝 짝:홀짝게임에 짝을 걸고 참가합니다.\n" + "!랭킹:랭킹을 확인합니다.").queue();
		}

		if (msg.equals("!도박참여")) {
			if (PlayerInfo.setPlayer(tag)) {
				channel.sendMessage(user.getAsMention() + "님이 참여하셨습니다. (잔액:" + PlayerInfo.getPoint(tag) + "원)").queue();
			}
		}

		if (msg.equals("!잔액")) {
			if (PlayerInfo.contain(tag)) {
				channel.sendMessage(user.getAsMention() + "님의 잔액은 " + PlayerInfo.getPoint(tag) + "원 입니다.").queue();
			}
		}

		if (msg.equals("!홀짝 홀")) {
			if ((int) (Math.random() * 3) == 0) {
				if (PlayerInfo.contain(tag)) {
					PlayerInfo.addPoint(tag, PlayerInfo.getPoint(tag) / 2);

					channel.sendMessage(user.getAsMention() + "\n*\"홀\"이 나왔습니다. 현재 금액의 절반을 얻습니다.* \n.").queue();
				}
			} else {
				if (PlayerInfo.contain(tag)) {
					PlayerInfo.addPoint(tag, (int)(PlayerInfo.getPoint(tag) * -0.2));

					channel.sendMessage(user.getAsMention() + "\n*\"짝\"이 나왔습니다. 현재 금액의 20%를 잃습니다.*\n.").queue();
				}
			}
		}

		if (msg.equals("!홀짝 짝")) {
			if ((int) (Math.random() * 3) == 0) {
				if (PlayerInfo.contain(tag)) {
					PlayerInfo.addPoint(tag, PlayerInfo.getPoint(tag) / 2);

					channel.sendMessage(user.getAsMention() + "\n*\"짝\"이 나왔습니다. 현재 금액의 절반을 얻습니다.* \n.").queue();
				}
			} else {
				if (PlayerInfo.contain(tag)) {
					PlayerInfo.addPoint(tag, (int)(PlayerInfo.getPoint(tag) * -0.2));

					channel.sendMessage(user.getAsMention() + "\n*\"홀\"이 나왔습니다. 현재 금액의 20%을 잃습니다.*\n.").queue();
				}
			}
		}

		if (msg.equals("!랭킹")) {
			List<Entry<String, Integer>> list_entries = new ArrayList<Entry<String, Integer>>(PlayerInfo.player.entrySet());

			// 비교함수 Comparator를 사용하여 내림 차순으로 정렬
			Collections.sort(list_entries, new Comparator<Entry<String, Integer>>() {
				// compare로 값을 비교
				public int compare(Entry<String, Integer> obj1, Entry<String, Integer> obj2)
				{
					// 내림 차순으로 정렬
					return obj2.getValue().compareTo(obj1.getValue());
				}
			});
			
			String rankingMsg = "-랭킹-\n";
			
			int cnt = 0;
			for(Entry<String, Integer> entry : list_entries) {
				String[] name = entry.getKey().split("#");
				rankingMsg += "\n" + ++cnt + "위:" + name[0] + "(잔액:" + entry.getValue() + "원)";
			}
			
			if(rankingMsg.equals("-랭킹-\n")) {
				channel.sendMessage("게임에 참가한 사람이 없습니다.").queue();
			}
			else {
				channel.sendMessage(rankingMsg).queue();
			}
		}
	}
}