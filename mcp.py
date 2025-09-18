
import asyncio
from mcp import McpServer, tool

class MyServer:
    """
    Ein einfacher MCP-Server, der ein Echo-Tool zur Verfügung stellt.
    """
    @tool
    async def echo(self, message: str) -> str:
        """
        Gibt die empfangene Nachricht zurück.
        """
        print(f"Echo-Tool aufgerufen mit: {message}")
        return message

async def main():
    """
    Die Hauptfunktion zum Starten des Servers.
    """
    server = McpServer(MyServer(), transport="stdio")
    await server.run()

if __name__ == "__main__":
    print("MCP-Server wird gestartet...")
    asyncio.run(main())


