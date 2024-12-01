import streamlit as st
st.set_page_config(
    page_title="Computer Networks",
    layout="wide",
)
# Sidebar setup
st.sidebar.title("Computer Networks")

# Sidebar options using a selectbox
menu = st.sidebar.selectbox(
    'Click to Choose Program',
    [
        "StopWait and SlidingWindow",
        "Socket Client Server Model",
        "ARP & RARP",
        "PING & TraceRoute",
        "Socket or HTTP for Web Pages",
        "Remote Procedure Call",
        "Subnetting",
        "Application of TCP Socket",
        "Case Study : Routing Algorithms"
    ]
)

# Display dynamic title
st.title(f"{menu}")

# Logic for each menu option
if menu == "StopWait and SlidingWindow":
    st.text("StopWait.java")
    stopwait = """
import java.util.Scanner;

class StopWait {
    public static boolean sendFrame(int frame) {
        System.out.println("Frame " + frame + " sent.");
        return true;
    }
    public static boolean receiveAcknowledgment(int frame) {
        System.out.println("Acknowledgment for Frame " + frame + " received.");
        return true;
    }
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Enter the total number of frames to send: ");
            int totalFrames = sc.nextInt();
            System.out.println("Stop-and-Wait Protocol Simulation");
            int currentFrame = 0;
            while (currentFrame < totalFrames) {
                System.out.println("Sending Frame " + currentFrame);
                boolean frameSent = sendFrame(currentFrame);
                if (frameSent) {
                    boolean ackReceived = receiveAcknowledgment(currentFrame);
                    if (ackReceived) {
                        System.out.println("Frame " + currentFrame + " acknowledged.");
                        currentFrame++;
                    } else {
                        System.out.println("No acknowledgment for Frame " + currentFrame + ", resending...");
                    }
                }
            }
            System.out.println("All frames sent successfully.");
        }
    }
}
"""
    st.code(stopwait, language="java")

    st.text("SlidingWindow.java")
    slidingwindow = """
import java.util.Scanner;

class SlidingWindowProtocol {
    public static boolean sendFrame(int frame) {
        System.out.println("Frame " + frame + " sent.");
        return true;
    }
    public static boolean receiveAcknowledgment(int frame) {
        System.out.println("Acknowledgment for Frame " + frame + " received.");
        return true;
    }
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Enter the total number of frames to send: ");
            int totalFrames = sc.nextInt();
            System.out.print("Enter the window size: ");
            int windowSize = sc.nextInt();
            System.out.println("\nSliding Window Protocol Simulation (Go-Back-N)\n");
            int sentFrame = 0;
            int acknowledgedFrame = 0;
            while (acknowledgedFrame < totalFrames) {
                for (int i = 0; i < windowSize && sentFrame < totalFrames; i++) {
                    sendFrame(sentFrame);
                    sentFrame++;
                }
                for (int i = acknowledgedFrame; i < sentFrame; i++) {
                    boolean ackReceived = receiveAcknowledgment(i);
                    if (ackReceived) {
                        System.out.println("Frame " + i + " acknowledged.\n");
                        acknowledgedFrame++;
                    } else {
                        System.out.println("Acknowledgment lost for Frame " + i + ". Resending frames starting from Frame " + acknowledgedFrame + "...\n");
                        sentFrame = acknowledgedFrame;
                        break;
                    }
                }
            }
            System.out.println("All frames sent and acknowledged successfully.");
        }
    }
}
"""
    st.code(slidingwindow, language="java")

elif menu == "Socket Client Server Model":
    st.text("Server.java")
    server_code = """
import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) {
        int port = 6666;
        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("Server is listening on port " + port);
            while (true) {
                Socket socket = serverSocket.accept();
                System.out.println("New client connected");
                try (
                    InputStream input = socket.getInputStream();
                    BufferedReader reader = new BufferedReader(new InputStreamReader(input));
                    OutputStream output = socket.getOutputStream();
                    PrintWriter writer = new PrintWriter(output, true)
                ) {
                    String message = reader.readLine();
                    System.out.println("Received from client: " + message);
                    writer.println("Hello Client, you said: " + message);
                } finally {
                    socket.close();
                }
            }
        } catch (IOException ex) {
            System.out.println("Server error: " + ex.getMessage());
            ex.printStackTrace();
        }
    }
}
"""
    st.code(server_code, language="java")

    st.text("Client.java")
    client_code = """
import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) {
        int port = 6666;
        try (Socket socket = new Socket("localhost", port)) {
            System.out.println("Connected to server");
            try (
                OutputStream output = socket.getOutputStream();
                PrintWriter writer = new PrintWriter(output, true);
                InputStream input = socket.getInputStream();
                BufferedReader reader = new BufferedReader(new InputStreamReader(input))
            ) {
                writer.println("Hello Server!");
                String response = reader.readLine();
                System.out.println("Server response: " + response);
            }
        } catch (IOException ex) {
            System.out.println("Client error: " + ex.getMessage());
        }
    }
}
"""
    st.code(client_code, language="java")

elif menu == "ARP & RARP":
    st.text("ARP.java")
    arp_code = """
    import java.util.HashMap;
public class ARP {
    HashMap<String, String> arpTable = new HashMap<>();
    void sendARPRequest(String ip) {
        System.out.println("Sending ARP Request for IP: " + ip);
        String mac = "00:1A:2B:3C:4D:5E";
        arpTable.put(ip, mac); 
        System.out.println("Received MAC: " + mac + " for IP: " + ip);
    }
    public static void main(String[] args) {
        new ARP().sendARPRequest("192.168.1.1");
    }
}"""
    st.code(arp_code, language="java")
    st.text("RARP.java")
    rarp_code = """import java.util.HashMap;
public class RARP {
    HashMap<String, String> rarpTable = new HashMap<>();
    void sendRARPRequest(String mac) {
        System.out.println("Sending RARP Request for MAC: " + mac);
        String ip = "192.168.1.100"; // Dummy IP address
        rarpTable.put(mac, ip); 
        System.out.println("Received IP: " + ip + " for MAC: " + mac);
    }
    public static void main(String[] args) {
        new RARP().sendRARPRequest("00:1A:2B:3C:4D:5E");
    }
}"""
    st.code(rarp_code, language="java")
    # Same structure for ARP and RARP code
    pass

elif menu == "PING & TraceRoute":
    st.text("PING.java")
    ping_code = """
    import java.io.IOException;
import java.net.InetAddress;
import java.util.Scanner;
public class PING {
    public static void main(String[] args) throws InterruptedException {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter IP or hostname to ping: ");
        String host = scanner.nextLine();
        try {
            InetAddress inet = InetAddress.getByName(host);
            for (int i = 1; i <= 100; i++) {
                long start = System.currentTimeMillis();
                if (inet.isReachable(1000)) {
                    System.out.println("Reply from " + host + ": time=" + (System.currentTimeMillis() - start) + "ms");
                } else {
                    System.out.println("Request timed out.");
                }
                Thread.sleep(100);
            }
        } catch (IOException e) {
            System.out.println("Host unreachable: " + e.getMessage());
        }
        scanner.close();
    }
}"""
    st.code(ping_code, language="java")
    st.text("TraceRoute.java")
    tracert_code = """
    import java.io.*;
import java.util.Scanner;
public class TraceRoute {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter host to trace route: ");
        String host = scanner.nextLine();
        try {
            ProcessBuilder pb = new ProcessBuilder("tracert", host);
            Process process = pb.start();
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
            process.waitFor();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            scanner.close();
        }
    }
}"""   
    st.code(tracert_code, language="java")
    # Same structure for PING and TraceRoute code
    pass

elif menu == "Socket or HTTP for Web Pages":
    st.text("ImageServer.java")
    image_server_code = """
import java.io.*;
import java.net.*;
import java.nio.file.*;
import java.util.*;

public class ImageServer {
    private static final int PORT = 7777;
    private static final String UPLOAD_DIR = "uploads/";

    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket(PORT);
        System.out.println("Server started at http://localhost:" + PORT);
        
        File uploadDir = new File(UPLOAD_DIR);
        if (!uploadDir.exists()) {
            uploadDir.mkdir();
        }

        while (true) {
            Socket clientSocket = serverSocket.accept();
            handleClient(clientSocket);
        }
    }

    private static void handleClient(Socket clientSocket) {
        try (BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
             OutputStream out = clientSocket.getOutputStream()) {

            String line = in.readLine();
            if (line == null) return;

            String[] request = line.split(" ");
            String method = request[0];
            String path = request[1];
            if (method.equals("GET")) {
                handleGetRequest(out, path);
            } else if (method.equals("POST")) {
                handlePostRequest(in, out, path, clientSocket);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void handleGetRequest(OutputStream out, String path) throws IOException {
        if (path.equals("/")) {
            sendResponse(out, "200 OK", "text/html", getHtmlForm());
        } else if (path.startsWith("/uploads/")) {
            File file = new File(UPLOAD_DIR + path.substring(9));
            if (file.exists()) {
                sendFileResponse(out, file);
            } else {
                sendResponse(out, "404 Not Found", "text/html", "<h1>File not found</h1>");
            }
        } else {
            sendResponse(out, "404 Not Found", "text/html", "<h1>Page not found</h1>");
        }
    }

    private static String getHtmlForm() {
        return \"\"\"
<html>
<head>
    <title>Image Upload</title>
    <style>
        /* CSS styles here */
    </style>
</head>
<body>
    <h1>Upload Image</h1>
    <form method="POST" enctype="multipart/form-data" action="/">
        <input type="file" name="file" accept="image/*">
        <input type="submit" value="Upload">
    </form>
</body>
</html>
\"\"\";
    }
}
"""
    st.code(image_server_code, language="java")
    
elif menu == "Remote Procedure Call":
    st.text("Server.java")
    server_code = """
    import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.server.UnicastRemoteObject;
import java.util.Scanner;

public class Server extends UnicastRemoteObject implements Calculator {
    public Server() throws RemoteException { super(); }
    public int add(int a, int b) { return a + b; }
    public int subtract(int a, int b) { return a - b; }
    public int multiply(int a, int b) { return a * b; }
    public double divide(int a, int b) {
        if (b == 0) throw new ArithmeticException("Cannot divide by zero.");
        return (double) a / b;
    }
    public int modulus(int a, int b) { return a % b; }
    public double exponent(int a, int b) { return Math.pow(a, b); }
    public double squareRoot(int a) { return Math.sqrt(a); }
    public double logarithm(int a) { return Math.log(a); }
    public static void main(String[] args) {
        try {
            Server calculatorServer = new Server();
            Scanner scanner = new Scanner(System.in);
            System.out.print("Enter the port number: ");
            int port = scanner.nextInt();
            LocateRegistry.createRegistry(port);
            Naming.rebind("rmi://localhost:" + port + "/CalculatorService", calculatorServer);
            System.out.println("Server is ready for operation...");
        } catch (Exception e) {
            System.err.println("Exception occurred: " + e.getMessage());
        }
    }
}"""
    st.code(server_code, language="java")
    st.text("Client.java")
    client_code = """
    import java.rmi.Naming;
import java.util.Scanner;
public class Client {
    public static void main(String[] args) {
        try {
            Calculator calculator = (Calculator) Naming.lookup("rmi://localhost:6666/CalculatorService");
            Scanner scanner = new Scanner(System.in);
            System.out.println("Choose an operation: ");
            System.out.println("1. Addition");
            System.out.println("2. Subtraction");
            System.out.println("3. Multiplication");
            System.out.println("4. Division");
            System.out.println("5. Modulus");
            System.out.println("6. Exponent");
            System.out.println("7. Square Root");
            System.out.println("8. Logarithm");
            System.out.print("Enter Your Choice: ");
            int choice = scanner.nextInt();

            System.out.print("Enter the first number: ");
            int num1 = scanner.nextInt();
            System.out.print("Enter the second number: ");
            int num2 = scanner.nextInt();
            
            
            switch (choice) {
                case 1:
                    System.out.println("Result of addition: " + calculator.add(num1, num2));
                    System.out.println("Operation Success...");
                    break;
                case 2:
                    System.out.println("Result of subtraction: " + calculator.subtract(num1, num2));
                    System.out.println("Operation Success...");
                    break;
                case 3:
                    System.out.println("Result of multiplication: " + calculator.multiply(num1, num2));
                    System.out.println("Operation Success...");
                    break;
                case 4:
                    try {
                        System.out.println("Result of division: " + calculator.divide(num1, num2));
                        System.out.println("Operation Success...");
                    } catch (ArithmeticException e) {
                        System.out.println("Error: " + e.getMessage());
                    }
                    break;
                case 5:
                    System.out.println("Result of modulus: " + calculator.modulus(num1, num2));
                    System.out.println("Operation Success...");
                    break;
                case 6:
                    System.out.println("Result of exponent: " + calculator.exponent(num1, num2));
                    System.out.println("Operation Success...");
                    break;
                case 7:
                    System.out.println("Result of square root: " + calculator.squareRoot(num1));
                    System.out.println("Operation Success...");
                    break;
                case 8:
                    System.out.println("Result of logarithm: " + calculator.logarithm(num1));
                    System.out.println("Operation Success...");
                    break;
                default:
                    System.out.println("Invalid choice. Please select a valid operation.");
                    System.out.println("Operation Failed...");
            }
            scanner.close();
        } catch (Exception e) {
            System.err.println("Exception occurred: " + e.getMessage());
        }
    }
}"""
    st.code(client_code, language="java")
    st.text("Calculator.java")
    calculator_code = """
    import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Calculator extends Remote {
    int add(int a, int b) throws RemoteException;
    int subtract(int a, int b) throws RemoteException;
    int multiply(int a, int b) throws RemoteException;
    double divide(int a, int b) throws RemoteException;
    int modulus(int a, int b) throws RemoteException;
    double exponent(int a, int b) throws RemoteException;
    double squareRoot(int a) throws RemoteException;
    double logarithm(int a) throws RemoteException;
}"""
    st.code(calculator_code, language="java")
elif menu == "Subnetting":
    st.text("Subnetting.java")
    subnetting_code = """
    import java.net.InetAddress;
import java.net.UnknownHostException;
public class Subnetting {
    public static void main(String[] args) {
        try {
            InetAddress localHost = InetAddress.getLocalHost();
            String ipAddress = localHost.getHostAddress();
            System.out.println("Device IP Address: " + ipAddress);
            String subnetMask = "255.255.255.0";
            String binaryIP = ipToBinary(ipAddress);
            String binaryMask = ipToBinary(subnetMask);
            String networkAddress = calculateNetworkAddress(binaryIP, binaryMask);
            System.out.println("Network Address: " + binaryToIp(networkAddress));
            String broadcastAddress = calculateBroadcastAddress(networkAddress, binaryMask);
            System.out.println("Broadcast Address: " + binaryToIp(broadcastAddress));
            int numberOfHosts = (int) Math.pow(2, (32 - getCIDR(subnetMask))) - 2;
            System.out.println("Number of Hosts: " + numberOfHosts);
        } catch (UnknownHostException e) {
            System.out.println("Unable to get the IP address of the device.");
            e.printStackTrace();
        }
    }
    public static String ipToBinary(String ip) {
        String[] octets = ip.split("\\.");
        StringBuilder binaryIp = new StringBuilder();
        for (String octet : octets) {
            String binaryOctet = String.format("%8s", Integer.toBinaryString(Integer.parseInt(octet))).replace(' ', '0');
            binaryIp.append(binaryOctet);
        }
        return binaryIp.toString();
    }
    public static String binaryToIp(String binaryIp) {
        StringBuilder ip = new StringBuilder();
        for (int i = 0; i < binaryIp.length(); i += 8) {
            int octet = Integer.parseInt(binaryIp.substring(i, i + 8), 2);
            ip.append(octet).append(".");
        }
        return ip.substring(0, ip.length() - 1);
    }
    public static String calculateNetworkAddress(String ip, String mask) {
        StringBuilder networkAddress = new StringBuilder();
        for (int i = 0; i < ip.length(); i++) {
            networkAddress.append(ip.charAt(i) == '1' && mask.charAt(i) == '1' ? '1' : '0');
        }
        return networkAddress.toString();
    }
    public static String calculateBroadcastAddress(String networkAddress, String mask) {
        StringBuilder broadcastAddress = new StringBuilder();
        for (int i = 0; i < networkAddress.length(); i++) {
            broadcastAddress.append(mask.charAt(i) == '0' ? '1' : networkAddress.charAt(i));
        }
        return broadcastAddress.toString();
    }
    public static int getCIDR(String subnetMask) {
        return ipToBinary(subnetMask).replace("0", "").length();
    }
}
"""
    st.code(subnetting_code, language="java")
    
elif menu == "Application of TCP Socket":
    st.header("File Transfer using TCP Sockets")
    col1, col2 = st.columns(2)
    with col1:
        st.text("FileServer.java")
        file_server_code = """
        import java.io.*;
import java.net.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class FileServer {
    private static final int PORT = 1234;
    private static final String OUTPUT_DIR = "received_files/";
    private static final DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyyMMdd_HHmmss");

    public static void main(String[] args) {
        // Create output directory if it doesn't exist
        createOutputDirectory();
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            System.out.println("Server started successfully");
            System.out.println("Listening on port: " + PORT);
            System.out.println("Waiting for clients...\n");
            while (true) {
                try (Socket clientSocket = serverSocket.accept();
                     InputStream in = clientSocket.getInputStream();
                     FileOutputStream out = new FileOutputStream(OUTPUT_DIR + generateFileName())) {
                    in.transferTo(out);
                    String clientAddress = clientSocket.getInetAddress().getHostAddress();
                    System.out.println("File received successfully from " + clientAddress);
                    System.out.println("Waiting for next client...\n");
                } catch (IOException e) {
                    System.err.println("Error handling client: " + e.getMessage());
                }
            }
        } catch (IOException e) {
            System.err.println("Server error: " + e.getMessage());
            System.err.println("Could not listen on port: " + PORT);
            System.exit(1);
        }
    }

    private static void createOutputDirectory() {
        File directory = new File(OUTPUT_DIR);
        if (!directory.exists()) {
            if (directory.mkdirs()) {
                System.out.println("Created output directory: " + OUTPUT_DIR);
            } else {
                System.err.println("Failed to create output directory!");
                System.exit(1);
            }
        }
    }

    private static String generateFileName() {
        String timestamp = LocalDateTime.now().format(formatter);
        return "received_file_" + timestamp + ".txt";
    }
}"""
        st.code(file_server_code, language="java")
    with col2:
        st.text("FileClient.java")
        file_client_code = """
        import java.io.*;
import java.net.*;

public class FileClient {
    public static void main(String[] args) throws IOException {
        if (args.length != 1) { System.out.println("Usage: java FileClient <file_path>"); return; }
        try (Socket socket = new Socket("localhost", 1234);
             FileInputStream in = new FileInputStream(args[0]);
             OutputStream out = socket.getOutputStream()) {
            in.transferTo(out);
            System.out.println("File sent");
        }
    }
}"""
        st.code(file_client_code, language="java")
    st.markdown("""---""") 
    st.header("ECHO Server-Client Application")
    col1, col2 = st.columns(2)

    with col1:
        st.text("echoServer.java")
        echo_server_code = """
        import java.io.*;
import java.net.*;
public class Server {
    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(3000)) {
            System.out.println("Hello Jayanthan,\nServer has started in PORT :"+"6666");
            while (true) {
                try (Socket clientSocket = serverSocket.accept();
                     BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                     PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true)) {
                    
                    String message;
                    while ((message = in.readLine()) != null) {
                        out.println(message);
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}"""
        st.code(echo_server_code, language="java")
    with col2:
        st.text("echoClient.java")
        echo_client_code = """
        import java.io.*;
import java.net.*;
public class Client {
    public static void main(String[] args) {
        try (Socket socket = new Socket("localhost", 3000);
             BufferedReader consoleInput = new BufferedReader(new InputStreamReader(System.in));
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()))) {
             
            String input;
            while ((input = consoleInput.readLine()) != null) {
                out.println(input);  // Send input to server
                System.out.println("Echo Response: " + in.readLine());  // Print echoed response
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}"""
        st.code(echo_client_code, language="java")

    st.markdown("""---""")  # This adds the horizontal line after the two code blocks
    
    
    st.header("Chat Application using TCP Sockets")
    col1, col2 = st.columns(2)

    with col1:
        st.text("chatServer.java")
        chat_server_code = """
        import java.io.*;
        import java.net.*;

        public class ChatServer {
            public static void main(String[] args) {
                try (ServerSocket serverSocket = new ServerSocket(12345)) {
                    System.out.println("Server started. Waiting for client...");
                    Socket socket = serverSocket.accept();
                    System.out.println("Client connected.");

                    BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                    PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

                    String message;
                    while ((message = in.readLine()) != null) {
                        System.out.println("Client: " + message);
                        out.println("Server: " + message); // Echo message back to client
                    }

                    socket.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
        """
        st.code(chat_server_code, language="java")

    with col2:
        st.text("chatClient.java")
        chat_client_code = """
        import java.io.*;
        import java.net.*;

        public class ChatClient {
            public static void main(String[] args) {
                try (Socket socket = new Socket("localhost", 12345);
                     BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                     PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
                     BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in))) {

                    System.out.println("Connected to server. Type messages:");

                    String message;
                    while ((message = userInput.readLine()) != null) {
                        out.println(message); // Send message to server
                        System.out.println(in.readLine()); // Print server's response
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
        """
        st.code(chat_client_code, language="java")

    st.markdown("""---""")
    
# Case Study : Routing Algorithms
elif menu == "Case Study : Routing Algorithms":
    st.header("Case Study on Routing Algorithms")

    # Link State Routing Section
    with st.expander("i. Link State Routing"):
        st.subheader("Aim: To Study the Link State Routing")
        st.write("""
        Routing is the process of selecting the best paths in a network. In the past, routing was also 
        used to mean forwarding network traffic among networks. This study focuses on routing in 
        electronic data networks using packet-switching technology.
        """)
        st.markdown("### Routing Overview")
        st.write("""
        - Routing directs packet forwarding (logically addressed packets) from their source to the ultimate 
          destination through intermediate nodes (e.g., routers, gateways).
        - Routing tables in a router's memory are critical for efficient routing.
        """)
        st.markdown("### Key Routing Elements")
        st.write("""
        1. **Prefix-Length**: Longer subnet masks are preferred.
        2. **Metric**: Lower metric (cost) is preferred.
        3. **Administrative Distance**: Lower distance is preferred across protocols.
        """)
        st.write("""
        Structured addressing (used in routing) allows better scalability and performance compared to 
        unstructured addressing (bridging). This makes routing the dominant form of addressing on the Internet.
        """)

    # Flooding Section
    with st.expander("ii. Flooding"):
        st.subheader("Flooding")
        st.write("""
        Flooding is a simple routing algorithm where every incoming packet is sent through all 
        outgoing links except the one it arrived on. This algorithm is commonly used in:
        - Bridging
        - Usenet
        - Peer-to-peer file sharing
        - Routing protocols like OSPF, DVMRP, and ad-hoc wireless networks.
        """)
        st.markdown("### Types of Flooding")
        st.write("""
        1. **Uncontrolled Flooding**: All nodes route packets indefinitely, leading to issues like broadcast storms.
        2. **Controlled Flooding**:
            - **SNCF (Sequence Number Controlled Flooding)**: Nodes track sequence numbers to avoid duplicates.
            - **RPF (Reverse Path Flooding)**: Packets are forwarded only along valid paths.
        """)
        st.markdown("### Algorithm Steps")
        st.write("""
        1. Each node acts as both a transmitter and a receiver.
        2. Each node forwards every message to all neighbors except the source node.
        """)
        st.markdown("### Advantages of Flooding")
        st.write("""
        - Packets are guaranteed delivery if a path exists.
        - Shortest paths are naturally utilized.
        - Simple to implement.
        """)
        st.markdown("### Disadvantages of Flooding")
        st.write("""
        - High bandwidth usage due to redundant packets.
        - Risk of infinite loops without precautions like:
            - Hop count or time-to-live counters.
            - Memory to track packets and forward each only once.
            - Loop-free topology enforcement.
        """)

    # Distance Vector Routing Section
    with st.expander("iii. Distance Vector Routing"):
        st.subheader("Distance Vector Routing")
        st.write("""
        Distance-vector routing protocols calculate paths using algorithms like:
        - Bellman–Ford Algorithm
        - Ford–Fulkerson Algorithm
        - DUAL FSM (used in Cisco protocols)
        """)
        st.markdown("### Key Features")
        st.write("""
        - Routers periodically inform neighbors of topology changes, reducing computational complexity.
        - Routing decisions are based on:
            1. Direction (next hop or exit interface).
            2. Distance (cost to destination).
        """)
        st.markdown("### Examples of Distance Vector Protocols")
        st.write("""
        - **RIP (Routing Information Protocol)**: Uses hop count as the metric.
        - **IGRP (Interior Gateway Routing Protocol)**: Considers node delay and bandwidth.
        """)
        st.markdown("### Count-to-Infinity Problem")
        st.write("""
        A major issue in distance-vector protocols:
        - When a router goes offline, neighbors may incorrectly propagate outdated paths, 
          causing loops and metric inflation until the problem resolves.
        - Example:
            - Router A goes offline.
            - Router B receives updates from C (unaware of A’s status) and propagates incorrect information.
        - Solutions include:
            - Limiting hop counts.
            - Split horizon and route poisoning techniques.
        """)

    # Conclusion
    st.info("This case study analyzed three key routing algorithms: Link State, Flooding, and Distance Vector Routing. Each has unique strengths, applications, and challenges.")
