from dnslib import DNSRecord, RR, TXT
from dnslib.server import DNSServer, BaseResolver
from google.generativeai import GenerativeModel, configure
import asyncio

# Configuration
GEMINI_API_KEY = "AIzaSyCxaR2mP5afNSzIQc6Zg5GxSN6cPLUJu6s"  # Replace with your key
DNS_PORT = 8000
MODEL_NAME = "gemini-1.5-flash"

# Initialize Gemini
configure(api_key=GEMINI_API_KEY)
model = GenerativeModel(MODEL_NAME)

class AIResolver(BaseResolver):
    def __init__(self):
        self.loop = asyncio.new_event_loop()
        super().__init__()

    async def generate_answer(self, question):
        response = await model.generate_content_async(
            f"Answer in one word or short sentence: {question}"
        )
        return response.text

    def resolve(self, request, handler):
        reply = request.reply()
        qname = str(request.q.qname)
        clean_question = qname.replace('.', ' ').strip()
        
        try:
            answer = self.loop.run_until_complete(
                self.generate_answer(clean_question)
            )
            reply.add_answer(RR(
                rname=request.q.qname,
                rtype=16,  # TXT record type
                rdata=TXT(answer),
                ttl=60
            ))
        except Exception as e:
            reply.add_answer(RR(
                rname=request.q.qname,
                rtype=16,
                rdata=TXT(f"Error: {str(e)}"),
                ttl=10
            ))
        
        return reply

if __name__ == '__main__':
    print(f"Starting DNS AI responder on port {DNS_PORT}...")
    resolver = AIResolver()
    udp_server = DNSServer(
        resolver=resolver,
        port=DNS_PORT,
        address="0.0.0.0"
    )
    udp_server.start_thread()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        udp_server.stop()
        print("\nServer stopped")