# !pip install nltk
import string
import datetime as dt
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
class chatbot:
    negative_response=["bye","later","quit","exit","end"]
    current_time=dt.datetime.now().strftime("%B %d, %Y")
    general_question= {
                        "Hii":"Hello",
                        "Hello":"Hi",
                        "human":"I am Anti Ai, not a human or a robot.",
                        "robot":"I am an AI language model developed by Anti Ai, not a human or a robot.",
                        "name":"Anti Chatbot, an AI companion.",
                        "age":"I don’t have an age since I’m an artificial intelligence.",
                        "date ":f"Today is {current_time}",
                        "motto":"अन्ते सत्यं विजयते।",
        "About company Anti":"AntiAI is an AI research and development company. Our mission is to ensure that the threat from artificial general intelligence are mitigated even before they arise.\n\nWe believe that humanity should benefit from AI, and we're developing our own first-in-class Anti AI software to ensure safe usage.We are building safe and smart solutions against AGI, but will also consider our mission fulfilled if our work aids others to achieve this outcome.",
        "vision":"Our mission is to ensure that the threat from artificial general intelligence are mitigated even before they arise.\n\nWe believe that humanity should benefit from AI",
        "contact":"https://antiai.ltd/"
        
}
    
    response={"AI Services":"Advanced Protection for Your Digital AssetsIn today's digital age, protecting your data and systems from cyber threats is more criticalthan ever. Our AI Security services provide advanced protection for your digital assets,utilizing cutting-edge machine learning algorithms to detect and prevent cyber threats inreal-time. Here's a detailed look at our AI Security offerings:",
             "Real-time Threat Detection":"Our AI-powered security systems monitor your digital assets 24/7, detecting potential threats in real-time. By analyzing patterns and anomalies in network traffic, user behavior, and system logs, our machine learning algorithms can identify and alert you to potential security breaches before they cause damage. This proactive approach to security ensures that your data and systems remain secure, even in the face of sophisticated cyber threats.",
             "Automated Incident Response":" In the event of a security breach, our AI-driven incident response system kicks into action, automatically isolating affected systems, containing the threat, and initiating recovery procedures. This rapid response minimizes the impact of security incidents, reducing downtime and preventing data loss. Our automated incident response system is customizable, allowing you to tailor the response to your specific needs and requirements.",
             "Machine Learning-based Anomaly Detection":"Our AI security services leverage advanced machine learning algorithms to identify unusual patterns and anomalies in your digital environment. By continuously learning from your data, our system can adapt to new threats and evolving attack patterns, ensuring that your security measures remain effective over time. This adaptive approach to security ensures that your digital assets are protected against even the most sophisticated cyber threats.",
              "Compliance and Risk Management":"Our AI security services help you maintain compliance with industry regulations and standards, such as GDPR, HIPAA, and PCI DSS. By continuously monitoring your digital environment for potential compliance issues, our system can alert you to potential risks and help you take corrective action before they become a problem. Our compliance and risk management services also include regular security audits and assessments, ensuring that your security measures remain up-to-date and effective.",
              "Security Analytics and Reporting":": Our AI security services provide detailed analytics and reporting, giving you insights into your security posture and helping you make informed decisions about your security strategy. Our customizable dashboards and reports allow you to track key security metrics, identify trends, and monitor your security performance over time. This data-driven approach to security ensures that you have the information you need to make informed decisions about your security strategy.",
              "Web Services":"Custom Solutions for Your Business Needs Our Web Development services offer end-to-end solutions for building robust, scalable, and user-friendly websites and applications. Here's a detailed look at our Web Development offerings",
              "Custom Application Development":"Our team of experienced developers can build custom web applications tailored to your business needs. From concept to deployment, we work closely with you to ensure that your application meets your requirements and exceeds your expectations. Our custom application development services include requirements gathering, design, development, testing, and deployment.",
              "Content Management System (CMS)":"We specialize in building custom CMS solutions that allow you to manage your website's content with ease. Our CMS solutions are user-friendly, scalable, and customizable, ensuring that you have the tools you need to manage your website effectively. Our CMS solutions include popular platforms such as WordPress, Drupal, and Joomla, as well as custom-built solutions tailored to your specific needs",
              "Ecommerce Development:":": Our Ecommerce development services help you build and manage your online store, from product catalog management to payment processing and order fulfillment. We specialize in building custom Ecommerce solutions that are tailored to your business needs, ensuring that your online store is user-friendly, secure, and scalable. Our Ecommerce development services include popular platforms such as Shopify, Magento, and WooCommerce, as well as custom-built solutions.",
              "MEAN Stack Development":"Our team of experienced developers can build custom web applications using the MEAN stack (MongoDB, Express.js, AngularJS, and Node.js). This powerful combination of technologies allows us to build scalable, high-performance web applications that meet your business needs. Our MEAN stack development services include requirements gathering, design, development, testing, and deployment",
              "MERN Stack Development":"Our team of experienced developers can also build custom web applications using the MERN stack (MongoDB, Express.js, React.js, and Node.js). This popular combination of technologies allows us to build modern, responsive web applications that are tailored to your business needs. Our MERN stack development services include requirements gathering, design, development, testing, and deployment.",
              "Social Media Apps":"Our team can build custom social media applications that allow you to engage with your audience and build your brand. From social networking platforms to messaging apps, we can help you build a social media presence that meets your business needs. Our social media app development services include requirements gathering, design, development, testing, and deployment",
              "DevOps Services":"Streamlining Software Development and Deployment Our DevOps services help organizations streamline their software development and deployment processes. Here's a detailed look at our DevOps offerings:",
              "Continuous Integration/Continuous Deployment ( CICD )":"Ops offerings: Continuous Integration/Continuous Deployment (CI/CD): Our CI/CD services help you automate your software development and deployment processes, reducing time-to-market and improving software quality. By continuously integrating and deploying code changes, our system ensures that your software is always up-to-date and ready for release. Our CI/CD services include popular tools such as Jenkins, Travis CI, and CircleCI",
              "Infrastructure as Code (IaC)":"s such as Jenkins, Travis CI, and CircleCI. Infrastructure as Code (IaC): Our IaC services help you manage your infrastructure as code, allowing you to automate infrastructure provisioning, configuration, and management. By treating your infrastructure as code, you can ensure consistency, reproducibility, and scalability across your environment. Our IaC services include popular tools such as Terraform, Ansible, and Chef",
              "Configuration Management":"Our configuration management services help you manage your software and infrastructure configurations, ensuring consistency and reproducibility across your environment. By automating configuration management, you can reduce errors, improve efficiency, and ensure that your systems are always up-to-date. Our configuration management services include popular tools such as Puppet, Chef, and Ansible",
              "DevOps Consulting and Implementation":"ols such as Puppet, Chef, and Ansible. DevOps Consulting and Implementation: Our DevOps consulting and implementation services help you design and implement a DevOps strategy that meets your business needs. From assessing your current processes to designing and implementing a custom DevOps solution, we work closely with you to ensure that your DevOps strategy is effective, efficient, and aligned with your business goals. Our DevOps consulting and implementation services include requirements gathering, design, implementation, training, and support."
             }
              
    jobs=["You can look into our career page for more info regarding jobs"]

    
    def __init__(self):
        self.question()
        
        
    def question(self):
        self.input_quest=input("\nEnter Your Message (quit -->to exit):")
        if len(self.input_quest) < 3:
            print("Please enter at least 3 words OR Try with Full Form if any.")
            self.question()
            return
        self.quest=self.remove_punctuation(self.input_quest)
        
        from nltk.tokenize import RegexpTokenizer
        tokenizer=RegexpTokenizer(r'\w+|\$[\d\.]+|\S+')
        token=tokenizer.tokenize(self.quest)                                           # For reponse
        
        
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [t for t in token if t.lower() not in stop_words]

        # lower case the General Questions
        general_question_lowerCase= list(map(lambda x:x.lower(), chatbot.general_question))
        
  
        def score_match(key, token):
            key_tokens = tokenizer.tokenize(key)                                       # tokens of the data of genereal quest dictionary
            score = sum(1 for t in token if t.lower() in (k.lower() for k in key_tokens))
            return score

 
        self.best_match = None
        self.best_score = 0

     
        for key in self.general_question:
            self.score = score_match(key, filtered_tokens)
            if self.score > self.best_score:
                self.best_match = key
                self.best_score = self.score
                self.match_type = "general"

        if self.best_match:
            if self.match_type == "general":
                print(f"{self.general_question[self.best_match]}")                     # Chat bot reply to general question
                                                                                       
        else:                                                                          # For Response dic
            response_keys = chatbot.response.keys()
            for tokens in filtered_tokens:
                matches = [response_keys_matched for response_keys_matched in response_keys if tokens.lower() in response_keys_matched.lower()]

                if len(matches)==1:
                    print(f"\n{matches[0]}: {chatbot.response[matches[0]]}")           # Replying to user when it matches with the data present in response
                    break
                elif tokens in ["job" ,"opening" ,"career","careers","jobs",'vaccancy',"openings"]:          # For the Job Search Query
                    self.job_search()
                    break
                elif len(matches)>=2:
                    for i in range(len(matches)):
                        print(f"\n{i+1}--> {matches[i]}")
                              
                    choice=self.get_valid_index(len(matches))                          # Making user to enter the valid type and number
                    print(f"\n{matches[choice-1]}: {chatbot.response[matches[choice-1]]}")
                    break
                    
                elif tokens in chatbot.negative_response:                              # TO QUIT FROM ChatBot
                    print("Hope to see you next time")
                    return
                             
            else:                                                                     # else came into play when for loops didnt get the appropriate result
                print("I am in Developing stage thats why not be able to answer this question")
            
        self.question()
        
    def job_search(self):
        print(chatbot.jobs)
        
    
    def get_valid_index(self, max_index):
        while True:
            try:
                inp = int(input("Kindly enter the index number: "))
                if 1 <= inp <= max_index:
                    return inp
                else:
                    print(f"Please enter a number between 1 and {max_index}.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.") 
                
    
    def remove_punctuation(self,text):
        translator = str.maketrans("", "", string.punctuation)
        cleaned_text = text.translate(translator)
        return cleaned_text
    
c=chatbot()
