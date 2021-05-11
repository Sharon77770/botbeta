package botbeta;

import javax.security.auth.login.LoginException;

import net.dv8tion.jda.api.JDABuilder;

public class Main {
	public static void main(String[] args) throws LoginException {
		JDABuilder jb = JDABuilder.createDefault("NzY5MDI2MDU1MjE4Mzk3MTk0.X5JBUw.LKBbFjzZLUrmX2NknaEHob3dUzg");
		jb.addEventListeners(new MyListener());
		jb.build();
	}
}