import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class App extends Frame{

    private TextField enter = new TextField();
    private TextField result = new TextField();
    private Choice fromChoice = new Choice();
    private Choice toChoice = new Choice();
    private Button convert = new Button("Convert");

    public App(){

        setLayout(new GridLayout(0, 5, 0, 10));
        setSize(550, 200);
        setTitle("Binary Decimal Hexadecimal convertor");

        //Image img = loadImage("applg.png");
        //setIconImage("applg.png");
        setIconImage(Toolkit.getDefaultToolkit().getImage("applg.png"));
        setResizable(false);

        Label from = new Label("From");
        add(from);

        fromChoice.add("Decimal");
        fromChoice.add("Binary");
        fromChoice.add("Hexadecimal");
        add(fromChoice);

        add(new Label()); // empty

        Label to = new Label("To");
        add(to);

        toChoice.add("Decimal");
        toChoice.add("Binary");
        toChoice.add("Hexadecimal");
        add(toChoice);

        add(new Label()); // empty

        add(enter);
        add(new Label()); // empty
        add(new Label()); // empty
        result.setEditable(false);
        add(result);
        add(new Label()); // empty
        add(new Label()); // empty

        ButtonControl button = new ButtonControl();
        convert.addActionListener(button);
        add(convert);

        // add window listener
        WindowControl window = new WindowControl();
        addWindowListener(window);
        setVisible(true);
    }

    public static void main(String[] args){
        new App();
    }

    // button class listener
    class ButtonControl implements ActionListener{
        public void actionPerformed(ActionEvent e){

            // get all arguments needed to convert
            String choice1 = fromChoice.getSelectedItem();
            String choice2 = toChoice.getSelectedItem();
            String numToConvert = enter.getText();

            // to check if it's working in console
            //System.out.println(choice1 + choice2 + numToConvert);
            try{
                ProcessBuilder process = new ProcessBuilder("python", "convertor.py", choice1, choice2, numToConvert);

                BufferedReader reader = new BufferedReader(new InputStreamReader(process.start().getInputStream()));
                String read = reader.readLine();
                result.setText(read);
            }
            catch(IOException exc){
                System.out.println("Error");
            }

        }
    }

    // window class listener
    class WindowControl implements WindowListener{
        @Override
        public void windowActivated(WindowEvent e) {}
        @Override
        public void windowClosed(WindowEvent e) {}
        @Override
        public void windowClosing(WindowEvent e) {System.exit(0);}
        @Override
        public void windowDeactivated(WindowEvent e) {}
        @Override
        public void windowDeiconified(WindowEvent e) {}
        @Override
        public void windowIconified(WindowEvent e) {}
        @Override
        public void windowOpened(WindowEvent e) {}
    }
}
