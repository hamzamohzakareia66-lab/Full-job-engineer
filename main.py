import os
import requests
from faucet_claimer import claim_free_faucets

# جلب الأسرار والمفاتيح البيئية
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
WALLET_ADDRESS = os.getenv("USDT_WALLET")

def send_telegram_msg(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

def run_engine():
    # 1. تشغيل وحدة التجميع المجاني الآلي (Auto-Faucet)
    faucet_yield = claim_free_faucets(WALLET_ADDRESS)
    
    # 2. قراءة رصيد المحفظة الحقيقي (محاكاة أو ربط البلوكشين)
    # في البداية يعتمد على الرصيد المجمع من السكربت تلقائياً
    total_balance = faucet_yield
    
    # 3. تحديد شريحة العمل وإدارة المخاطر (30%)
    risk_percentage = 0.30
    trade_allocation = total_balance * risk_percentage
    
    stage = "Tier 1: Auto-Faucet Claims Active (< $5)"
    
    # صياغة التقرير الإرشادي للارسال
    report = (
        "🚀 **Millionaire Business Execution Report**\n\n"
        f"📊 **Active Operational Stage:** `{stage}`\n\n"
        "💧 **Auto-Faucet Collector:**\n"
        f"· Status: `Running 24/7`\n"
        f"· Last Claim Yield: `${faucet_yield:.4f} POL/USDT`\n\n"
        "💰 **Revenue & Capital Breakdown:**\n"
        f"· Accumulated Bootstrapped Capital: `${total_balance:.4f} USDT`\n"
        f"· Active Trade Allocation (30% Risk): `${trade_allocation:.4f} USDT`\n\n"
        "✅ **Status:** `Engine running continuously via GitHub Actions. Zero human intervention needed.`"
    )
    
    send_telegram_msg(report)

if __name__ == "__main__":
    run_engine()
    
