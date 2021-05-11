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

		if (msg.equals("!����")) {
			channel.sendMessage("" + "-�����忡 ���Ű� ȯ���մϴ�!:D-\n" + "\n" + "�� ���� ���� �׽�Ʈ�߿� ������ ������ ���� �߰� �� �����Դϴ�.\n" + "\n"
					+ "-���� ��-\n" + "\n" + "-Ȧ¦ ����:Ȧ �Ǵ� ¦�� �����Ͽ� �����մϴ�.(�¸��� �ܾ��� 50% �߰� ȹ��, �й�� �ܾ��� 20%�ս�)\n" + "\n" + "*-��ɾ� ���-*\n"
					+ "\n" + "!��������:���ڿ� �����մϴ�. �� ��ɾ ����ؾ� ������ ��� �� �ֽ��ϴ�.\n"
					+ "!�ܾ�:���� ���� �ܾ��� Ȯ���մϴ�. �ܾ��� �������� ������ �δ��� ���������� ��ŷ�� ���� �� �ֽ��ϴ�.\n" + "!Ȧ¦ Ȧ:Ȧ¦���ӿ� Ȧ�� �ɰ� �����մϴ�.\n"
					+ "!Ȧ¦ ¦:Ȧ¦���ӿ� ¦�� �ɰ� �����մϴ�.\n" + "!��ŷ:��ŷ�� Ȯ���մϴ�.").queue();
		}

		if (msg.equals("!��������")) {
			if (PlayerInfo.setPlayer(tag)) {
				channel.sendMessage(user.getAsMention() + "���� �����ϼ̽��ϴ�. (�ܾ�:" + PlayerInfo.getPoint(tag) + "��)").queue();
			}
		}

		if (msg.equals("!�ܾ�")) {
			if (PlayerInfo.contain(tag)) {
				channel.sendMessage(user.getAsMention() + "���� �ܾ��� " + PlayerInfo.getPoint(tag) + "�� �Դϴ�.").queue();
			}
		}

		if (msg.equals("!Ȧ¦ Ȧ")) {
			if ((int) (Math.random() * 3) == 0) {
				if (PlayerInfo.contain(tag)) {
					PlayerInfo.addPoint(tag, PlayerInfo.getPoint(tag) / 2);

					channel.sendMessage(user.getAsMention() + "\n*\"Ȧ\"�� ���Խ��ϴ�. ���� �ݾ��� ������ ����ϴ�.* \n.").queue();
				}
			} else {
				if (PlayerInfo.contain(tag)) {
					PlayerInfo.addPoint(tag, (int)(PlayerInfo.getPoint(tag) * -0.2));

					channel.sendMessage(user.getAsMention() + "\n*\"¦\"�� ���Խ��ϴ�. ���� �ݾ��� 20%�� �ҽ��ϴ�.*\n.").queue();
				}
			}
		}

		if (msg.equals("!Ȧ¦ ¦")) {
			if ((int) (Math.random() * 3) == 0) {
				if (PlayerInfo.contain(tag)) {
					PlayerInfo.addPoint(tag, PlayerInfo.getPoint(tag) / 2);

					channel.sendMessage(user.getAsMention() + "\n*\"¦\"�� ���Խ��ϴ�. ���� �ݾ��� ������ ����ϴ�.* \n.").queue();
				}
			} else {
				if (PlayerInfo.contain(tag)) {
					PlayerInfo.addPoint(tag, (int)(PlayerInfo.getPoint(tag) * -0.2));

					channel.sendMessage(user.getAsMention() + "\n*\"Ȧ\"�� ���Խ��ϴ�. ���� �ݾ��� 20%�� �ҽ��ϴ�.*\n.").queue();
				}
			}
		}

		if (msg.equals("!��ŷ")) {
			List<Entry<String, Integer>> list_entries = new ArrayList<Entry<String, Integer>>(PlayerInfo.player.entrySet());

			// ���Լ� Comparator�� ����Ͽ� ���� �������� ����
			Collections.sort(list_entries, new Comparator<Entry<String, Integer>>() {
				// compare�� ���� ��
				public int compare(Entry<String, Integer> obj1, Entry<String, Integer> obj2)
				{
					// ���� �������� ����
					return obj2.getValue().compareTo(obj1.getValue());
				}
			});
			
			String rankingMsg = "-��ŷ-\n";
			
			int cnt = 0;
			for(Entry<String, Integer> entry : list_entries) {
				String[] name = entry.getKey().split("#");
				rankingMsg += "\n" + ++cnt + "��:" + name[0] + "(�ܾ�:" + entry.getValue() + "��)";
			}
			
			if(rankingMsg.equals("-��ŷ-\n")) {
				channel.sendMessage("���ӿ� ������ ����� �����ϴ�.").queue();
			}
			else {
				channel.sendMessage(rankingMsg).queue();
			}
		}
	}
}