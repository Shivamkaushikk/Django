from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
import pandas as pd

@api_view(['POST'])
@parser_classes([MultiPartParser])
def process_excel(request):
    file = request.FILES.get('file')
    if not file:
        return Response({"error": "No file uploaded"}, status=400)

    try:
        df = pd.read_excel(file)
        df['processed'] = df[df.columns[0]].astype(str).str.upper()
        return Response({"data": df.to_dict(orient='records')})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
